import json
import requests

gov_cms_api = 'https://cms-gov.makerfoundation.com/content/governance-dashboard?network=mainnet'
subgraph_api = 'https://api.thegraph.com/subgraphs/name/protofire/makerdao-governance-v1_5'
spells_query = """
{
    spells {
        id
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
            spell['title'] = spell['id']
        return spells
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, spells_query))

def all_spells():
    spells = get_spells()
    all_spells = []
    for spell in spells:
        if float(spell['approvals']) > 50:
            spell['approvals'] = str(round(float(spell['approvals']), 2)).rjust(10, ' ')
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
    spells = get_spell_titles(set_hat(previous_spell(all_spells())))
    spells.sort(key=lambda x: float(x['approvals']), reverse=True)

    trim_title = 70

    message = "" # "Spell count at block _{}_\n".format('blockID')
    for spell in spells:
        if spell['hat']:
            message = message + "> {} | [{}]({}) :tophat:\n".format(spell['approvals'], spell['title'][:trim_title], spell['link'])
        elif spell['prev_cast']:
            message = message + "> {} | [{}]({}) :back:\n".format(spell['approvals'], spell['title'][:trim_title], spell['link'])
        elif spell ['active']:
            message = message + "> {} | [{}]({}) :up:\n".format(spell['approvals'], spell['title'][:trim_title], spell['link'])
        else:
            message = message + "> {} | [{}]({})\n".format(spell['approvals'], spell['title'], spell['link'])

    message = message + "[Executive Votes on mkrgov.science]({})".format(mkrgov_domain + 'executive')

    return message

print(print_spells())
