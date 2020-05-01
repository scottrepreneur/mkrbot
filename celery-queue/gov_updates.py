import json
import time
from mkrgov import get_spells, get_polls, get_poll_title, mkrgov_domain
from mkrbot import bot_response

voting_dashboard = "https://vote.makerdao.com"

def check_new_spell():
    # get spells from file
    with open('./spells.json') as json_file:
        spells_data = json.load(json_file)

    # spells query
    spells_query_data = get_spells()

    # remove spells in file
    for _spell in spells_data:

        for ind, spell in enumerate(spells_query_data):
            if spell['id'].lower() == _spell['id'].lower():
                del(spells_query_data[ind])
                break

    # print outstanding spell
    if len(spells_query_data) > 0:
        for spell in spells_query_data:
            new_spell_message = f'''
New Spell: [{spell['title']}]({mkrgov_domain + 'executive/' + spell['id']}) :wiz: [Vote Now!]({voting_dashboard})
'''

            bot_response('user', new_spell_message, 'governance-and-risk', False)

            spells_data.append({
                "id": spell['id'],
                "casted": spell['casted'],
                "title": spell['title'],
                "lifted": spell['lifted'],
                "timestamp": spell['timestamp']
            })

    # write new spell to file
    with open('./spells.json', 'w') as outfile:
        json.dump(spells_data, outfile)

    return True

def check_cast_spell():
    # check 'non-expired' spells from file, mark old ones expired
    with open('./spells.json') as json_file:
        spells_data = json.load(json_file)

    uncast_spells = []
    for ind, spell in enumerate(spells_data):
        if not spell['casted']:
            uncast_spells.append(spell)
    
    # print(uncast_spells)
    spells_query_data = get_spells()

    # check if those spells have been cast since last check
    for spell in spells_data:
        for _spell in spells_query_data:
            if spell['id'] == _spell['id']:
                if not spell['casted'] and not spell['lifted']:
                    if _spell['casted'] or spell['lifted']:
                        spell['casted'] = _spell['casted']
                        spell['lifted'] = _spell['lifted']

                        spell_cast_message = f'''
[{spell['title'] or spell['id']}]({mkrgov_domain}executive/{spell['id']}) was cast on {time.strftime("%d/%m/%Y at %H:%M", time.gmtime(int(spell['casted'])))} UTC.
[You can still help secure the governance system]({voting_dashboard})
'''

                        # output spell
                        bot_response('user', spell_cast_message, 'governance-and-risk, False)

    # update cast spell in file
    with open('./spells.json', 'w') as outfile:
        json.dump(spells_data, outfile)
    
    return True

def check_new_poll():
    # get polls from file
    with open('./polls.json') as json_file:
        polls_data = json.load(json_file)

    # check pollingemitter for polls
    polls_query_data = get_polls()

    # remove polls in file
    for poll in polls_data:

        for ind, _poll in enumerate(polls_query_data):
            if int(poll['pollId']) == int(_poll['pollId']):
                del(polls_query_data[ind])
                break

    # print outstanding spell
    if len(polls_query_data) > 0:
        for poll in polls_query_data:
            poll_title = get_poll_title(poll)

            new_poll_message = f'''
New Governance Poll: [{poll_title}]({mkrgov_domain + 'poll/' + poll['pollId']}). :clipboard: [Vote Now!]({voting_dashboard})
'''
            # print(new_poll_message)
            bot_response('user', new_poll_message, 'governance-and-risk', False)

            polls_data.append({
                "id": poll['id'],
                "creator": poll['creator'],
                "pollId": poll['pollId'],
                "title": poll_title,
                "endDate": poll['endDate'],
                "startDate": poll['startDate'],
                "url": poll['url'],
                "votesCount": poll['votesCount']
            })

    # write new poll to file
    with open('./polls.json', 'w') as outfile:
        json.dump(polls_data, outfile)

    return True
