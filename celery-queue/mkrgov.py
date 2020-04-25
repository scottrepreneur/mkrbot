import json
import requests

gov_cms_api = 'https://cms-gov.makerfoundation.com/content/governance-dashboard?network=mainnet'
subgraph_api = 'https://api.thegraph.com/subgraphs/name/scottrepreneur/maker-governance'
mkrgov_domain = 'https://mkrgov.science/'
spells_query = '''
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
'''
polls_query = '''
{
    polls {
        id
        creator
        url
        pollId
        startDate
        endDate
        votesCount
    }
}
'''
governance_overview_query = '''
{
    governanceInfo(id: "0x0") {
        id
        countProxies
        countAddresses
        countSlates
        countCasted
        countSpells
        countLock
        countFree
        countPolls
        locked
        lastBlock
        lastSynced
        hat
    }
}
'''

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

def get_polls():
    response = requests.post(subgraph_api, json={'query': polls_query})
    if response.status_code == 200:
        polls = response.json()['data']['polls']
        return polls

def get_poll_title(poll):
    if not 'title' in poll.keys():
        if poll['url'] != 'test' and poll['url'][len(poll['url']) - 3:] == '.md':
            response = requests.get(poll['url'])
            poll_description = response.content.decode("utf-8")

            i1 = poll_description.find('title: ')
            i2 = poll_description.find('summary:')
            poll['title'] = poll_description[i1+7:i2 - 1]

    return poll['title']

# print(get_poll_titles(get_polls()))

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

def get_hat(spells):
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

    return hat

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

    with open('./spells.json') as json_file:
        spells_data = json.load(json_file)
    for _spell in spells_data:
        for spell in spells:
            if _spell['id'].casefold() == spell['id'].casefold() and spell['title'] == spell['id']:
                spell['title'] = _spell['title']

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


def governance_overview():
    response = requests.post(subgraph_api, json={'query': governance_overview_query})

    data = response.json()['data']['governanceInfo']
    hat = get_hat(get_spells())

    gov_message =  f'''
Governance Polls: {data['countPolls']} | Governing Proposal: [{hat['title']}]({hat['link']}) 
Executive Votes: {data['countSpells']} | Votes Passed: {data['countCasted']}
:mkr: Locked: {float(data['locked']):,.1f} | Voters: {data['countAddresses']}
'''

    return gov_message
