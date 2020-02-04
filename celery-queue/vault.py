
import os
import locale
from datetime import datetime
from dateutil.parser import parse
import requests

MAKER_GRAPH_URL = os.getenv('MAKER_GRAPH_URL')

locale.setlocale(locale.LC_ALL, 'en_US')

def get_vault_by_id(message):
    
    ## VAULT LOOKUP MESSAGE ##
    # ```VAULT ID: {ID} | Collateralization Ratio: {RATIO}
    # Outstanding Dai: {ART} Collateral Locked: {INK} (${INK_USD})
    # Last Action: {ACTION} {AMOUNT} at {TIME}
    # Owner: {LAD} {DELETED}
    # ````

    vault = message.split(' ')[1]

    get_vault_query = "{ getCup(id: " + str(vault) + ") {art,block,deleted,id,ink,ire,lad,pip,ratio,tab,time,actions {nodes {act,arg,time,pip}}}}"
    response = requests.post(MAKER_GRAPH_URL, json={'query': get_vault_query})
    cup = response.json()['data']['getCup']
    print(cup)
    
    vault_string = 'Vault ID: *[{id}]({vault_link})*\n'.format(
            id=cup['id'],
            vault_link='https://mkr.tools/cdp/' + str(cup['id'])
        )

    if cup['ratio'] == '0' or cup['ratio'] == 0 or cup['ratio'] == None:
        vault_string = vault_string + '```Collateralization Ratio: 0%\n'
    else:
        vault_string = vault_string + '```Collateralization Ratio: {ratio}\n'.format(
            ratio=str(round(float(cup['ratio']),2)) + '%',
        )
    
    # add outstanding dai
    if cup['art'] == '0' or cup['art'] == 0 or cup['art'] == None:
        vault_string = vault_string + 'Dai Drawn: 0 Dai | '
    else:
        vault_string = vault_string + 'Dai Drawn: {art} Dai | '.format(
            art=str(f"{round(float(cup['art']),2):,}")
        )

    # add collateral locked
    if cup['ink'] == '0' or cup['ink'] == 0 or cup['ink'] == None:
        vault_string = vault_string + 'Collateral: 0 ETH (~$0)\n'
    else:
        vault_string = vault_string + 'Collateral: {ink} ETH (~${ink_usd})\n'.format(
            ink=str(f"{round(float(cup['ink']),2):,}"),
            ink_usd=str(f"{round(float(cup['ink'])*float(cup['pip']),2):,}")
            )
    
    # add last action
    for action in cup['actions']['nodes']:
        # if ":" == action['time'][-3:-2]:
        #     action['time'] = action['time'][:-3] + action['time'][-2:]
        date = parse(action['time']).strftime('%b %d, %Y at %H:%M%p %Z')
        if action['act'] == 'SHUT' or action['act'] == 'OPEN':
            vault_string = vault_string + 'Last Action: {action_name} at {time}\n'.format(
                action_name=action['act'].capitalize(),
                time=str(date)
            )
        elif action['act'] == 'LOCK' or action['act'] == 'FREE':
            vault_string = vault_string + 'Last Action: {action_name} {amount} ETH at {time}\n'.format(
                action_name=action['act'].capitalize(),
                amount=str(f"{round(float(action['arg']),2):,}"),
                time=str(date)
                )
        elif action['act'] == 'DRAW' or action['act'] == 'WIPE':
            vault_string = vault_string + 'Last Action: {action_name} {amount} Dai at {time}\n'.format(
                action_name=action['act'].capitalize(),
                amount=str(f"{round(float(action['arg']),2):,}"),
                time=str(date)
                )
        break
        
    # add owner
    vault_string = vault_string + 'Owner: {owner}'.format(owner=cup['lad'])

    # if it's closed, mention 'deleted' #? most CDPs aren't formally closed, just emptied
    if cup['deleted']:
        vault_string = vault_string + ' | _CDP is Closed_```'
    else: 
        vault_string = vault_string + '```'
        
    return vault_string
    
