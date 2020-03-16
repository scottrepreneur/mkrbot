
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

    get_vault_query = f"{{ getCup(id: {str(vault)}) {{art,block,deleted,id,ink,ire,lad,pip,ratio,tab,time,actions {{nodes {{act,arg,time,pip}}}}}}}}"
    response = requests.post(MAKER_GRAPH_URL, json={'query': get_vault_query})
    cup = response.json()['data']['getCup']
    print(cup)

    id = cup['id']

    vault_link = f"https://mkr.tools/cdp/{str(id)}"
    vault_string = f'Vault ID: *[{str(id)}]({vault_link})*\n'
    
    if cup['ratio'] == '0' or cup['ratio'] == 0 or cup['ratio'] == None:
        vault_string = vault_string + '```Collateralization Ratio: 0%\n'
    else:
        ratio = str(round(float(cup['ratio']),2))
        vault_string = vault_string + f'```Collateralization Ratio: {ratio}%\n'
    
    # add outstanding dai
    if cup['art'] == '0' or cup['art'] == 0 or cup['art'] == None:
        vault_string = vault_string + 'Dai Drawn: 0 Dai | '
    else:
        art = str(round(float(cup['art']),2))
        vault_string = vault_string + f'Dai Drawn: {art} Dai | '

    # add collateral locked
    if cup['ink'] == '0' or cup['ink'] == 0 or cup['ink'] == None:
        vault_string = vault_string + 'Collateral: 0 ETH (~$0)\n'
    else:
        ink = str(round(float(cup['ink']),2))
        ink_usd = str(round(float(cup['ink']) * float(cup['pip']),2))
        vault_string = vault_string + f'Collateral: {ink} ETH (~${ink_usd})\n'
    
    # add last action
    for action in cup['actions']['nodes']:
        # if ":" == action['time'][-3:-2]:
        #     action['time'] = action['time'][:-3] + action['time'][-2:]
        action_name = action['act'].capitalize()
        time = str(parse(action['time']).strftime('%b %d, %Y at %H:%M%p %Z'))

        if action['act'] == 'SHUT' or action['act'] == 'OPEN':
            vault_string = vault_string + f'Last Action: {action_name} at {time}\n'

        elif action['act'] == 'LOCK' or action['act'] == 'FREE':
            amount = str(round(float(action['arg']),2))
            vault_string = vault_string + f'Last Action: {action_name} {amount} ETH at {time}\n'

        elif action['act'] == 'DRAW' or action['act'] == 'WIPE':
            amount = str(round(float(action['arg']),2))
            vault_string = vault_string + f'Last Action: {action_name} {amount} Dai at {time}\n'

        break
        
    # add owner
    vault_string = vault_string + f"Owner: {cup['lad']}"

    # if it's closed, mention 'deleted' #? most Vaults aren't formally closed, just emptied
    if cup['deleted']:
        vault_string = vault_string + ' | Vault is Closed```'
    else: 
        vault_string = vault_string + '```'
        
    return vault_string
    
