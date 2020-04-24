
import os
import locale
from datetime import datetime
from dateutil.parser import parse
import requests

MAKER_GRAPH_URL = os.getenv('MAKER_GRAPH_URL')

locale.setlocale(locale.LC_ALL, 'en_US')

def get_cdp_by_id(message):
    
    ## cdp LOOKUP MESSAGE ##
    # ```CDP ID: {ID} | Collateralization Ratio: {RATIO}
    # Outstanding Dai: {ART} Collateral Locked: {INK} (${INK_USD})
    # Last Action: {ACTION} {AMOUNT} at {TIME}
    # Owner: {LAD} {DELETED}
    # ````

    cdp = message.split(' ')[1]

    get_cdp_query = f"{{ getCup(id: {str(cdp)}) {{art,block,deleted,id,ink,ire,lad,pip,ratio,tab,time,actions {{nodes {{act,arg,time,pip}}}}}}}}"
    response = requests.post(MAKER_GRAPH_URL, json={'query': get_cdp_query})
    cup = response.json()['data']['getCup']
    print(cup)

    id = cup['id']

    cdp_link = f"https://mkr.tools/cdp/{str(id)}"
    cdp_string = f'CDP ID: *[{str(id)}]({cdp_link})*\n'
    
    if cup['ratio'] == '0' or cup['ratio'] == 0 or cup['ratio'] == None:
        cdp_string = cdp_string + '> Collateralization Ratio: 0%\n'
    else:
        ratio = str(round(float(cup['ratio']),2))
        cdp_string = cdp_string + f'> Collateralization Ratio: {ratio}%\n'
    
    # add outstanding dai
    if cup['art'] == '0' or cup['art'] == 0 or cup['art'] == None:
        cdp_string = cdp_string + '> Drawn: 0 :dai: | '
    else:
        art = str(round(float(cup['art']),2))
        cdp_string = cdp_string + f'> Drawn: {art:,.2f} :dai: | '

    # add collateral locked
    if cup['ink'] == '0' or cup['ink'] == 0 or cup['ink'] == None:
        cdp_string = cdp_string + 'Collateral: 0 :eth: (~$0)\n'
    else:
        ink = str(round(float(cup['ink']),2))
        ink_usd = str(round(float(cup['ink']) * float(cup['pip']),2))
        cdp_string = cdp_string + f'Collateral: {ink:,.2f} :eth: (~${ink_usd:,.0f})\n'
    
    # add last action
    for action in cup['actions']['nodes']:
        # if ":" == action['time'][-3:-2]:
        #     action['time'] = action['time'][:-3] + action['time'][-2:]
        action_name = action['act'].capitalize()
        time = str(parse(action['time']).strftime('%b %d, %Y at %H:%M%p %Z'))

        if action['act'] == 'SHUT' or action['act'] == 'OPEN':
            cdp_string = cdp_string + f'> Last Action: {action_name} at {time}\n'

        elif action['act'] == 'LOCK' or action['act'] == 'FREE':
            amount = str(round(float(action['arg']),2))
            cdp_string = cdp_string + f'> Last Action: {action_name} {amount:,.0f} :eth: at {time}\n'

        elif action['act'] == 'DRAW' or action['act'] == 'WIPE':
            amount = str(round(float(action['arg']),2))
            cdp_string = cdp_string + f'> Last Action: {action_name} {amount:,.0f} :dai: at {time}\n'

        break
        
    # add owner
    cdp_string = cdp_string + f"> Owner: {cup['lad']}"

    # if it's closed, mention 'deleted' #? most cdps aren't formally closed, just emptied
    if cup['deleted']:
        cdp_string = cdp_string + ' | cdp is Closed'
        
    return cdp_string
    
