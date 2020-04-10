import os
import re
import json
from datetime import datetime
from dateutil.parser import parse
import requests

MCD_VAULT_URL = os.getenv('MCD_VAULT_URL')

def get_vault_by_id(message):

    vault_id = message.split(' ')[1]
    response = requests.get(f'{MCD_VAULT_URL}/api/cdps/{vault_id}')
    actions = requests.get(f'{MCD_VAULT_URL}/api/cdps/{vault_id}/events')

    print(response.json())
    print(actions.json())
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
                print(f"current: {action['blockNum']} and last: {last_action['blockNum']}")
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

        else:
            vault_string = vault_string + f'> Last Action: {action["action-type"]} on {time}\n'

    # add owner
    vault_string = vault_string + f"> Owner: {data['userAddr']}"
        
    return vault_string
    
