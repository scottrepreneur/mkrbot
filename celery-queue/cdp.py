
import os
from datetime import datetime
from dateutil.parser import parse
import requests

MAKER_GRAPH_URL = os.getenv('MAKER_GRAPH_URL')

def get_cdp_by_id(message):
    
    ## CDP LOOKUP MESSAGE ##
    # ```CDP ID: {ID} | Collateralization Ratio: {RATIO}
    # Outstanding Dai: {ART} Collateral Locked: {INK} (${INK_USD})
    # Last Action: {ACTION} {AMOUNT} at {TIME}
    # Owner: {LAD} {DELETED}
    # ````

    cdp = message.split(' ')[1]

    get_cdp_query = "{ getCup(id: " + str(cdp) + ") {art,block,deleted,id,ink,ire,lad,pip,ratio,tab,time,actions {nodes {act,arg,time,pip}}}}"
    response = requests.post(MAKER_GRAPH_URL, json={'query': get_cdp_query})
    cup = response.json()['data']['getCup']
    print(cup)
    
    if cup['ratio'] == '0' or cup['ratio'] == 0 or cup['ratio'] == None:
        cdp_string = '```CDP ID: {id} | Collateralization Ratio: 0%\n'.format(
            id=cup['id']
        )
    else:
    # id and 
        cdp_string = '```CDP ID: {id} | Collateralization Ratio: {ratio}\n'.format(
            id=cup['id'],
            ratio=str(round(float(cup['ratio']),2)) + '%'
        )
    
    # add outstanding dai
    if cup['art'] == '0' or cup['art'] == 0 or cup['art'] == None:
        cdp_string = cdp_string + 'Outstanding Dai: 0 Dai | '
    else:
        cdp_string = cdp_string + 'Outstanding Dai: {art} Dai | '.format(
            art=str(round(float(cup['art']),2)))

    # add collateral locked
    if cup['ink'] == '0' or cup['ink'] == 0 or cup['ink'] == None:
        cdp_string = cdp_string + 'Collateral Locked: 0 ETH (~$0)\n'
    else:
        cdp_string = cdp_string + 'Collateral Locked: {ink} ETH (~${ink_usd})\n'.format(
            ink=str(round(float(cup['ink']),2)),
            ink_usd=str(round(float(cup['ink'])*float(cup['pip']),2))
            )
    
    # add last action
    for action in cup['actions']['nodes']:
        # if ":" == action['time'][-3:-2]:
        #     action['time'] = action['time'][:-3] + action['time'][-2:]
        date = parse(action['time']).strftime('%b %d, %Y at %H:%M%p %Z')
        if action['act'] == 'SHUT' or action['act'] == 'OPEN':
            cdp_string = cdp_string + 'Last Action: {action_name} at {time}\n'.format(
                action_name=action['act'].capitalize(),
                time=str(date)
            )
        elif action['act'] == 'LOCK' or action['act'] == 'FREE':
            cdp_string = cdp_string + 'Last Action: {action_name} {amount} ETH at {time}\n'.format(
                action_name=action['act'].capitalize(),
                amount=str(round(float(action['arg']),2)),
                time=str(date)
                )
        elif action['act'] == 'DRAW' or action['act'] == 'WIPE':
            cdp_string = cdp_string + 'Last Action: {action_name} {amount} Dai at {time}\n'.format(
                action_name=action['act'].capitalize(),
                amount=str(round(float(action['arg']),2)),
                time=str(date)
                )
        break
        
    # add owner
    cdp_string = cdp_string + 'Owner: {owner}'.format(owner=cup['lad'])

    # if it's closed, mention 'deleted' 
    if cup['deleted']:
        cdp_string = cdp_string + ' | _CDP is Closed_```'
    else: 
        cdp_string = cdp_string + '```'
        
    return cdp_string
    
