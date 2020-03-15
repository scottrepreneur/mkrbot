import json
import requests

gov_cms_api = 'https://cms-gov.makerfoundation.com/content/governance-dashboard?network=mainnet'
subgraph_api = 'https://api.thegraph.com/subgraphs/name/scottrepreneur/maker-governance'
spells_query = """
{
    spells {
        id
        description
        casted
        castedWith
        lifted
        liftedWith
        approvals
        totalVotes
        timestamp
        __typename
    }
}
"""
mkrgov_domain = "https://mkrgov.science/"
archived_spell_titles = [
    {
        "id": "0x8e5f3abc36da63142275202454c11237f47dd170",
        "title": "Activate the Savings Rate Spread and the Sai and Dai Stability Fee Adjustments."
    },
    {
        "id": "0xd24fbbb4497ad32308bda735683b55499ddc2cad",
        "title": "Activate the Dai Debt Ceiling Adjustment, Set Dai Savings Rate Spread, Set Sai Stability Fee, Lower Surplus Auction Bid, Set Governance Delay Module"
    },
    {
        "id": "0x333c0501182170c5002219380ded6b12c338e272",
        "title": "2020-01-03 Weekly Executive: DSR & SF to 6%"
    },
    {
        "id": "0xf44113760c4f70afeeb412c63bc713b13e6e202e",
        "title": "2019-11-19 Weekly Executive: Adjust Debt Ceilings"
    },
    {
       "id": "0xdd4aa99077c5e976afc22060eeafbbd1ba34eae9",
       "title": "2019-12-13 Weekly Executive: Adjust OSM parameters" 
    },
    {
        "id": "0x48916a2b11fa7a895426eedf9acf2d70523b1677",
        "title": "2020-01-31 Weekly Executive: Adjust SF 9%, DSR 8.75%, Debt Ceilings"
    },
    {
        "id": "0xde4000cb884b237efbd6f793584701230e1c45b3",
        "title": "2019-07-19 Weekly Executive"
    }
]

def get_spells():
    response = requests.post(subgraph_api, json={'query': spells_query})
    if response.status_code == 200:
        spells = response.json()['data']['spells']
        for spell in spells:
            spell['hat'] = False
            spell['active'] = False
            spell['prev_cast'] = False
            spell['link'] = mkrgov_domain + 'executive/' + spell['id']
            spell['title'] = spell['description'] or spell['id']
        return spells
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {spells_query}")

def all_spells():
    spells = get_spells()
    all_spells = []
    for spell in spells:
        if float(spell['approvals']) > 1000:
            spell['approvals'] = f"{float(spell['approvals']):.2f}"
            all_spells.append(spell)
    
    return all_spells

def set_hat(spells):
    index_of_hat = 0
    index_of_prev_hat = 0
    hat = {}
    for index, spell in enumerate(spells):
        if index == 0:
            index_of_hat = 0
            hat = spell
        else:
            if float(spell['approvals']) > float(hat['approvals']):
                index_of_hat = index
                hat = spell
                
    spells[index_of_hat]['hat'] = True
    
    return spells

def set_active(spells):
    for spell in spells:
        if not spell['casted']:
            spell['active'] = True
    
    return spells

def previous_spell(spells):
    prev_cast = {}
    cast_spells = []
    for spell in spells:
        if spell['casted']:
            cast_spells.append(spell)

    cast_spells.sort(key=lambda x: x['casted'], reverse=True)
    prev_cast = cast_spells[1]

    for spell in spells:
        if prev_cast['id'] == spell['id']:
            spell['prev_cast'] = True

    return spells

def get_active_spells():
    spells = set_active(get_spells())
    active_spells = []
    for spell in active_spells:
        if spell['active'] == True:
            active_spells.append(spell)
        
    return active_spells
    
def get_spell_titles(spells):
    gov_cms_data = requests.get(gov_cms_api).json()

    for vote in gov_cms_data:
        for proposal in vote['proposals']:
            for spell in spells:
                if proposal['source'].casefold() == spell['id'].casefold():
                    spell['title'] = proposal['title']

    for title in archived_spell_titles:
        for spell in spells:
            if title['id'].casefold() == spell['id'].casefold() and spell['title'] == spell['id']:
                spell['title'] = title['title']
    


    return spells

def print_spells():
    spells = get_spell_titles(set_hat(previous_spell(set_active(all_spells()))))
    spells.sort(key=lambda x: float(x['approvals']), reverse=True)

    trim_title = 70

    message = "" # "Spell count at block _{}_\n".format('blockID')
    for spell in spells:
        if spell['hat']:
            message = message + f"> `{spell['approvals'].rjust(10, ' ')}` | [{spell['title'][:trim_title]}]({spell['link']}) :tophat:\n"
        elif spell['prev_cast']:
            message = message + f"> `{spell['approvals'].rjust(10, ' ')}` | [{spell['title'][:trim_title]}]({spell['link']}) :back:\n"
        elif spell ['active']:
            message = message + f"> `{spell['approvals'].rjust(10, ' ')}` | [{spell['title'][:trim_title]}]({spell['link']}) :up:\n"
        elif spell['casted'] is not None:
            message = message + f"> `{spell['approvals'].rjust(10, ' ')}` | [{spell['title'][:trim_title]}]({spell['link']}) :heavy_check_mark:\n"
        else:
            message = message + f"> `{spell['approvals'].rjust(10, ' ')}` | [{spell['title']}]({spell['link']})\n"

    message = message + f"[Executive Votes on mkrgov.science]({mkrgov_domain + 'executive'})"

    return message
