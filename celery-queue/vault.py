import os
import re
import json
from datetime import datetime
from dateutil.parser import parse
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import web3

MCD_VAULT_URL = os.getenv('MCD_VAULT_URL')
MCD_VAULTS_SUBGRAPH = 'https://api.thegraph.com/subgraphs/name/graphitetools/maker'
NOMICS_API_KEY = os.getenv('NOMICS_API_KEY')
NOMICS_BASE_URL = 'https://api.nomics.com/v1/'
BURNED_URL = os.getenv('BURNED_URL')
EXPLORE_URL = os.getenv('EXPLORE_URL')

def get_vault_by_id(message):

    vault_id = message.split(' ')[1]
    response = requests.get(f'{MCD_VAULT_URL}/api/cdps/{vault_id}')
    actions = requests.get(f'{MCD_VAULT_URL}/api/cdps/{vault_id}/events')

    data = response.json()

    vault_link = f"https://defiexplore.com/cdp/{vault_id}"
    vault_string = f'Vault ID: *[{data["cdpId"]}]({vault_link})*\n'
    
    if data['ratio'] == '0' or data['ratio'] == 0 or data['ratio'] == None:
        vault_string = vault_string + '> Collateralization Ratio: 0% | '
    else:
        vault_string = vault_string + f'> Collateralization Ratio: {float(data["ratio"])*100:.2f}% | '
    
    if data['liqPrice'] == '0' or data['liqPrice'] == 0 or data['liqPrice'] == None:
        vault_string = vault_string + 'Liquidation Price: $0\n'
    else:
        vault_string = vault_string + f'Liquidation Price: ${float(data["liqPrice"])*100:,.2f}\n'
    
    # add outstanding dai
    if data['debt'] == '0' or data['debt'] == 0 or data['debt'] == None:
        vault_string = vault_string + '> Drawn: 0 :dai: | '
    else:
        vault_string = vault_string + f'> Drawn: {float(data["debt"]):,.2f} :dai: | '

    # add collateral locked
    if data['collateral'] == '0' or data['collateral'] == 0 or data['collateral'] == None:
        vault_string = vault_string + 'Collateral: 0 :eth: (~$0)\n'
    else:
        ink = float(data['collateral'])
        ink_usd = float(data['collateralUSD'])
        vault_string = vault_string + f'Collateral: {ink:,.2f} :eth: (~${ink_usd:,.2f})\n'
    
    # add last action
    last_action = {}
    if len(actions.json()) > 1:
        # print(actions)
        for action in actions.json():
            if last_action == {}:
                last_action = action

            else:
                # print(f"current: {action['blockNum']} and last: {last_action['blockNum']}")
                if action['blockNum'] > last_action['blockNum']:
                    last_action = action
    else:
        last_action = actions.json()[0]

    if last_action is not {}:
        # if ":" == action['time'][-3:-2]:
        #     action['time'] = action['time'][:-3] + action['time'][-2:]
        time = str(parse(last_action['timestamp']).strftime('%b %d, %Y at %H:%M%p %Z'))

        if last_action['actionType'] == 'Create':
            vault_string = vault_string + f'> Created vault on {time}\n'

        elif last_action['actionType'] == 'add-collateral':
            amount = float(action['collateral'])
            vault_string = vault_string + f'> Added {amount:,.2f} {action["type"]} on {time}\n'

        elif last_action['actionType'] == 'withdraw-collateral':
            amount = abs(float(action['collateral']))
            vault_string = vault_string + f'> Added Collateral {amount:,.2f} {action["type"]} on {time}\n'

        elif last_action['actionType'] == 'generate-dai':
            amount = float(action['debt'])
            vault_string = vault_string + f'> Generated {amount:,.2f} :dai: on {time}\n'

        elif last_action['actionType'] == 'payback-dai':
            amount = abs(float(action['debt']))
            vault_string = vault_string + f'> Paid back {amount:,.2f} :dai: on {time}\n'

        elif last_action['actionType'] == 'boost':
            vault_string = vault_string + f'> Boosted: Vault at {last_action["afterCDP"]["collateral"]} {last_action["type"]} and {last_action["afterCDP"]["debt"]} Dai\n'

        elif last_action['actionType'] == 'repay':
            vault_string = vault_string + f'> Repaid: Vault at {last_action["afterCDP"]["collateral"]} {last_action["type"]} and {last_action["afterCDP"]["debt"]} Dai\n'

        else:
            vault_string = vault_string + f'> Last Action: {action["actionType"]} on {time}\n'

    # add owner
    vault_string = vault_string + f"> Owner: {data['userAddr']}"
        
    return vault_string

def get_vaults_by_collateral_query(collateral_type):

    _transport = RequestsHTTPTransport(
        url=MCD_VAULTS_SUBGRAPH,
        use_json=True,
    )

    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,)

    vaults_query = gql("""
        query vaultsOverviewQuery($collateral: String!, $batch: Int!, $increment: Int!) {
            vaults(where: {collateral: $collateral}, first: $batch, skip: $increment) {
                id
                cdp {
                    id
                }
                debt
                supply
                }
            }
        """)
    
    vaults = []

    i = 0
    while i < 10:
        batch = 1000
        increment = i * batch
        
        params = {
            "collateral": collateral_type,
            "batch": batch,
            "increment": increment
        }

        vaults_response = client.execute(vaults_query, params)['vaults']

        if len(vaults_response) == 0:
            break; 
        else:
            if len(vaults) == 0:
                vaults = vaults_response
            else:
                vaults.extend(vaults_response)
        
        i = i + 1

    return vaults

# print(get_vaults_query("ETH-A"))

def collateral_vaults_overview(collateral):

    vaults = 0
    vaults_with_debt = 0
    locked = 0
    debt = 0

    vaults_query = get_vaults_by_collateral_query(collateral)
     
    for vault in vaults_query:
        vaults = vaults + 1

        if float(vault['debt']) > 0:
            vaults_with_debt = vaults_with_debt + 1
            debt = debt + float(vault['debt']) / 10 ** 18

        if float(vault['supply']) > 0:
            locked = locked + float(vault['supply']) / 10 ** 18

    _collateral = collateral.split('-')[0]

    data = requests.get(f"{NOMICS_BASE_URL}currencies/ticker?key={NOMICS_API_KEY}&ids={_collateral}&interval=1d,30d&convert=USD")
    supply = float(data.json()[0]['circulating_supply'])

    burned = requests.get(BURNED_URL).json()
    dai_cap = burned[f'mcd_dai_cap_{_collateral.lower()}']
    apr = (burned[f'mcd_fee_{_collateral.lower()}'] ** (60 * 60 * 24 * 365) - 1) * 100

    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()
    price = float(prices[f'{_collateral.lower()}FuturePrice'])

    return f"""
:{_collateral.lower()}: Vaults: {vaults:,.0f} | Locked: {locked:,.1f} | % Locked: {locked / supply * 100:.1f}%
Vaults with Debt: {vaults_with_debt:,.0f} ({vaults_with_debt / vaults * 100:.0f}%) | Collateralization Ratio: {(debt / (price * locked)) * 1000:.1f}%
Total Debt: {debt:,.0f} Dai | Mean Debt: {debt / vaults_with_debt:,.1f} Dai
Debt Ceiling: {dai_cap:,.0f} ({debt / dai_cap * 100:,.0f}%) | Stability Fee: {apr:.1f}%
"""

# print(collateral_vaults_overview("BAT-A"))

def bat_vaults():
    return collateral_vaults_overview("BAT-A")

def eth_vaults():
    return collateral_vaults_overview("ETH-A")

def usdc_vaults():
    return collateral_vaults_overview("USDC-A")

def get_all_vaults_query():
    _transport = RequestsHTTPTransport(
        url=MCD_VAULTS_SUBGRAPH,
        use_json=True,
    )

    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,)

    all_vaults_query = gql("""
        query vaultsOverviewQuery($batch: Int!, $increment: Int!) {
            vaults(first: $batch, skip: $increment) {
                id
                cdp {
                    id
                }
                collateral {
                    id
                }
                debt
                supply
                }
            }
        """)
    
    vaults = []

    i = 0
    while i < 10:
        batch = 1000
        increment = i * batch
        
        params = {
            "batch": batch,
            "increment": increment
        }

        vaults_response = client.execute(all_vaults_query, params)['vaults']

        if len(vaults_response) == 0:
            break; 
        else:
            if len(vaults) == 0:
                vaults = vaults_response
            else:
                vaults.extend(vaults_response)
        
        i = i + 1

    return vaults


def vaults_overview():

    vaults = 0
    vaults_with_debt = 0
    eth_locked = 0
    bat_locked = 0
    usdc_locked = 0
    debt = 0

    vaults_query = get_all_vaults_query()
     
    for vault in vaults_query:
        vaults = vaults + 1

        if float(vault['debt']) > 0:
            vaults_with_debt = vaults_with_debt + 1
            debt = debt + float(vault['debt']) / 10 ** 18

        if float(vault['supply']) > 0:
            if vault['collateral']['id'] == 'ETH-A':
                eth_locked = eth_locked + float(vault['supply']) / 10 ** 18
            elif vault['collateral']['id'] == 'BAT-A':
                bat_locked = bat_locked + float(vault['supply']) / 10 ** 18
            elif vault['collateral']['id'] == 'USDC-A':
                usdc_locked = usdc_locked + float(vault['supply']) / 10 ** 18

    burned = requests.get(BURNED_URL).json()
    dai_cap = burned[f'dai_cap']

    prices = requests.get(f'{EXPLORE_URL}/api/stats/globalInfo').json()
    eth_price = float(prices[f'ethFuturePrice'])
    bat_price = float(prices[f'batFuturePrice'])
    usdc_price = float(prices[f'usdcFuturePrice'])

    locked_value = eth_locked * eth_price + bat_locked * bat_price + usdc_price * usdc_locked

    return f"""
Vaults: {vaults:,.0f} | Vaults with Debt: {vaults_with_debt:,.0f} ({vaults_with_debt / vaults * 100:.0f}%)
Total Debt: {debt:,.0f} Dai | Debt Ceiling: {dai_cap:,.0f} Dai ({debt / dai_cap * 100:,.0f}%) 
Collateralization Ratio: {(debt / locked_value) * 1000:.1f}%
"""
