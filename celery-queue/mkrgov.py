import requests

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

def get_spells():
    response = requests.post(subgraph_api, json={'query': spells_query})
    if response.status_code == 200:
        spells = response.json()['data']['spells']
        for spell in spells:
            spell['hat'] = False
            spell['active'] = False
            spell['prev_cast'] = False
        return spells
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, spells_query))

def all_spells():
    spells = get_spells()
    all_spells = []
    for spell in spells:
        if float(spell['approvals']) > 50:
            spell['approvals'] = str(round(float(spell['approvals']), 2))
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

def print_spells():
    spells = set_hat(previous_spell(all_spells()))

    message = "" # "Spell count at block _{}_\n".format('blockID')
    for spell in spells:
        if spell['hat']:
            message = message + "> :tophat: {} Count: {}\n".format(spell['id'], spell['approvals'])
        elif spell['prev_cast']:
            message = message + "> last: {} Count: {}\n".format(spell['id'], spell['approvals'])
        elif spell ['active']:
            message = message + "> active: {} Count: {}\n".format(spell['id'], spell['approvals'])
        else:
            message = message + "> {} Count: {}\n".format(spell['id'], spell['approvals'])

    return message
