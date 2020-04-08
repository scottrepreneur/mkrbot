import os
import re
import difflib
from rocket import rocket

from triggers import mkrbot_triggers
from responses import mkrbot_responses

from cdp import get_cdp_by_id
from dai import dai_supply
from mkr import mkr_burned
from mkrgov import print_spells, mkrgov_domain
from vault import get_vault_by_id

ENVIRONMENT = os.getenv('ENVIRONMENT')

mkrbot_names = [
    '@mkr.bot',
    '@mkrbot',
    'mkr.bot',
    'mkrbot',
    'bot'
]

def mkrbot_message(user, message, channel):
    message = message.strip()
    print(message)
    
    # need to escape loop after command is found
    command_found = False
    while not command_found:
        # look through all the trigger groups
        for trigger_group in mkrbot_triggers:

            # look through each query set
            for query in mkrbot_triggers[trigger_group]:

                # handle non-queries here for simple matching
                if trigger_group == 'lost':
                    for sub in mkrbot_triggers[trigger_group][query]:
                        if message.casefold() == sub.casefold():
                            command_found = True
                            bot_response(user, mkrbot_responses[trigger_group][query], channel, False)

                elif trigger_group != 'queries':
                    for sub in mkrbot_triggers[trigger_group][query]:

                        if message.casefold() == sub.casefold():
                            command_found = True
                            bot_response(user, mkrbot_responses[trigger_group][query], channel, True)

                # handle queries here so regex can be used and pass parameters to functions
                else:
                    for sub in mkrbot_triggers[trigger_group][query]:

                        # depending on the query, regex match
                        if query == 'spell_count':
                            if message.casefold() == sub.casefold():
                                command_found = True
                                bot_response(user, print_spells(), channel, False)

                        elif query == 'check_vault':
                            if re.compile(sub).match(message):
                                command_found = True
                                bot_response(user, get_vault_by_id(message), channel, False)
                        
                        elif query == 'check_cdp':
                            if re.compile(sub).match(message):
                                command_found = True
                                bot_response(user, get_cdp_by_id(message), channel, False)

                        elif query == 'mkr_burned':
                            if message.casefold() == sub.casefold():
                                command_found = True
                                bot_response(user, mkr_burned(), channel, False)

                        elif query == 'dai_supply':
                            if message.casefold() == sub.casefold():
                                command_found = True
                                bot_response(user, dai_supply(), channel, False)
        
        # don't send two commands
        if command_found:
            break;
        else:               # otherwise send no commands found
            command_found = True
            bot_response(user, mkrbot_responses['lost']['no_commands'], channel, False)

def bot_response(_user, _message, _channel, _unfurl):
    # print only on Dev
    if ENVIRONMENT == 'DEVELOPMENT':
        print(_message)
        
    else:
        if _unfurl:
            rocket.send_message(_message, _channel, [{}])
        else:
            rocket.send_message(
                _message, 
                _channel, 
                [{
                    "title": "Maker Spells",
                    "text": "blah"
                }]
            )
