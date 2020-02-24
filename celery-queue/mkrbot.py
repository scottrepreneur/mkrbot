import os
import re
import difflib
from rocket import channels, rocket

from check_hat import check_spells
from vault import get_vault_by_id
from mkrgov import print_spells

MAKER_COMMUNITY_PORTAL = os.getenv('MAKER_COMMUNITY_PORTAL')
MKRBOT_GUIDE_URL = "https://community-development.makerdao.com/faqs/mkrbot-guide"
CONTRIBUTING_URL = "https://www.github.com/scottrepreneur/mkrbot/CONTRIBUTING"
CREATOR_DM_URL = "https://chat.makerdao.com/direct/scottrepreneur"

ENVIRONMENT = os.getenv('ENVIRONMENT')

#? bot admin
# TODO handle channel delegation
# TODO respond/tag specific users?

#? first commands
# TODO Update check spells command to use jernjml's version/ updating

#? new updates
# TODO Add MKR Burn makerburn.com
# TODO Integrate Governance CMS API
# TODO add oracle price feeds

mkrbot_names = [
    '@mkr.bot',
    '@mkrbot',
    'mkr.bot',
    'mkrbot',
    'bot'
]

mkrbot_triggers = {
    'queries': {                                #? trigger_group
        'spell_count': [                        #? query
            'spell',                            #? sub-query/command
            'spells',
            'spell count',
            'spells count',
            'chief spells',
            'chief spells count',
            'chief spell count',
            'what is the spell count',
            'what is the spell count?',
            'what is spell count',
            'what is spell count?',
            'mkr on spells',
            'mkr on spell',
            'mkr per spells',
            'mkr per spell'
        ],
        'check_vault':[
            'cdp [0-9]',
            'vault [0-9]'
        ]
    },
    'faqs': {
        'cdp': [
            'faqs cdp',
            'faq cdp',
            'cdp faqs',
            'cdp faq',
            'what is a cdp',
            'what is cdp',
            'what is a cdp?',
            'what is cdp?'
        ],
        'dai': [
            'faqs dai',
            'faq dai',
            'dai faqs',
            'dai faq',
            'what is dai',
            'what is dai?'
        ],
        'dsr': [
            'faqs dsr',
            'faq dsr',
            'dsr faqs',
            'dsr faq',
            'what is the dsr',
            'what is the dsr?',
            'what is dsr',
            'what is dsr?',
            'what is the dai savings rate',
            'what is the dai savings rate?',
            'what is dai savings rate',
            'what is dai savings rate?'
        ],
        'emergency_shutdown': [
            'faqs shutdown',
            'faq shutdown',
            'faq emergency shutdown',
            'shutdown faqs',
            'shutdown faq',
            'emergency shutdown faqs',
            'emergency shutdown faq',
            'what is emergency shutdown',
            'what is emergency shutdown?'
        ],
        'glossary': [
            'glossary',
            'terms',
            'faq glossary',
            'faq terms'
        ],
        'governance': [
            'faqs governance',
            'faq governance',
            'governance faqs',
            'governance faq',
            'what is governance',
            'what is governance?'
        ],
        'keepers': [
            'faqs keepers',
            'faqs keeper',
            'faq keepers',
            'faq keeper',
            'keepers faqs',
            'keeper faqs',
            'keepers faq',
            'keeper faq',
            'what is a keeper',
            'what is a keeper?',
            'what is keeper',
            'what is keeper?',
            'what is keepers',
            'what is keepers?'
        ],
        'liquidation': [
            'faqs liquidation',
            'faq liquidation',
            'liquidation faqs',
            'liquidation faq',
            'what is liquidation',
            'what is liquidation?'
        ],
        'makerdao': [
            'faqs maker',
            'faq maker',
            'maker faqs',
            'maker faq',
            'faq makerdao',
            'faqs makerdao',
            'makerdao faq',
            'makerdao faqs',
            'what is maker',
            'what is makerdao',
            'what is maker?',
            'what is makerdao?'
        ],
        'oracles': [
            'faqs oracles',
            'faqs oracle',
            'faq oracles',
            'faq oracle',
            'oracles faqs',
            'oracle faqs',
            'oracles faq',
            'oracle faq',
            'what is an oracle',
            'what is an oracle?'
        ],
        'risk_management': [
            'faqs risk',
            'faq risk',
            'risk faqs',
            'risk faq',
            'risk management faq',
            'risk management faqs',
            'faq risk management',
            'faqs risk management',
            'what is risk',
            'what is risk?',
            'what is risk management',
            'what is risk management?'
        ],
        'stability_fee': [
            'faqs stability',
            'faq stability',
            'faq stability fee',
            'faqs stability fee',
            'stability faqs',
            'stability fee faqs',
            'stability faq',
            'stability fee faq',
            'what is the stability fee',
            'what is the stability fee?',
            'what is stability fee',
            'what is stability fee?'
        ],
        'vault': [
            'faqs vaults',
            'faq vaults',
            'faq vault',
            'faqs vault'
            'vault faqs',
            'vault faq',
            'what is a vault',
            'what is a vault?',
            'what is vault',
            'what is vault?'
        ],
        'faqs_overview': [
            'faq',
            'faqs',
            'faqs list',
            'faqs overview',
            'faqs help',
            'faq list',
            'faq overview',
            'faq help'
        ]
    },
    'resources': {
        'dev_docs': [
            'docs',
            'dev docs',
            'documentation',
            'dev documentation',
            'developer documentation',
            'developer docs'
        ],
        'cdp_portal': [
            'portal',
            'cdp portal',
            'cdps portal',
            'portal cdp',
            'portal cdps'
        ],
        'oasis_app': [
            'oasis',
            'vault portal',
            'vaults portal',
            'portal vault',
            'portal vaults'
        ],
        'oasis_save': [
            'oasis save',
            'save'
        ],
        'oasis_trade': [
            'oasis trade',
            'trade'
        ],
        'governance_dashboard': [
            'governance',
            'gov',
            'vote',
            'gov dashboard',
            'governance dashboard',
            'governance portal',
            'portal governance',
        ],
        'awesome_makerdao': [
            'awesome',
            'awemkr',
            'am',
            'amd',
            'awesome makerdao',
            'awesomemakerdao',
            'awesomemaker'
        ],
        'awesome_channels': [
            'awesome channels',
            'awesome channel',
            'awesome maker channels',
            'awesome official channels',
            'awesome official maker channels',
            'amd channels',
            'amd maker channels',
            'amd official channels'
        ],
        'awesome_spend_dai': [
            'awesome spend',
            'awesome spend dai',
            'awesome dai spend',
            'amd spend',
            'amd spend dai',
            'amd dai spend'
        ],
        'awesome_use_dai': [
            'awesome use',
            'awesome use dai',
            'awesome dai use',
            'amd use',
            'amd use dai',
            'amd dai use'
        ],
        'awesome_lend_dai': [
            'awesome lend',
            'awesome lend dai',
            'awesome dai lend',
            'amd lend',
            'amd lend dai',
            'amd dai lend'
        ],
        'awesome_watch_dai': [
            'awesome watch',
            'awesome watch dai',
            'awesome dai watch',
            'amd watch',
            'amd watch dai',
            'amd dai watch'
        ],
        'awesome_hold_dai': [
            'awesome hold',
            'awesome hold dai',
            'awesome dai hold',
            'amd hold',
            'amd hold dai',
            'amd dai hold'
        ],
        'awesome_trade_dai': [
            'awesome trade',
            'awesome trade dai',
            'awesome dai trade',
            'amd trade',
            'amd trade dai',
            'amd dai trade'
        ],
        'awesome_dev_resoures': [
            'awesome dev',
            'awesome dev resources',
            'awesome dev resource',
            'awesome developer',
            'awesome developer resources',
            'awesome developer resource',
            'amd dev',
            'amd dev resources',
            'amd developer',
            'amd developer resources'
        ],
        'awesome_audits_security': [
            'awesome audit',
            'awesome audits',
            'amd audit',
            'amd audits'
        ],
        'awesome_overview': [
            'amd list',
            'amd overview',
            'amd help'
        ]
    },
    'lost': {
        'help': [
            'help'
        ]
    }
}

language_code = '/en'
faqs_url = '/makerdao-mcd-faqs/faqs'
mkrbot_responses = {
    'faqs': {
        'cdp': 'Heads up! CDPs are called Vaults in Multi-Collateral Dai\nhttps://community-development.makerdao.com/makerdao-mcd-faqs/faqs/vault',
        'dai': MAKER_COMMUNITY_PORTAL + faqs_url + '/dai',
        'dsr': MAKER_COMMUNITY_PORTAL + faqs_url + '/dsr',
        'emergency_shutdown': MAKER_COMMUNITY_PORTAL + faqs_url + '/emergency-shutdown',
        'governance': MAKER_COMMUNITY_PORTAL + '/makerdao-scd-faqs/scd-faqs' + '/governance',
        'glossary': MAKER_COMMUNITY_PORTAL + faqs_url + '/glossary',
        'keepers': MAKER_COMMUNITY_PORTAL + '/makerdao-scd-faqs/scd-faqs' + '/keepers',
        'liquidation': MAKER_COMMUNITY_PORTAL + faqs_url + '/liquidation',
        'makerdao': MAKER_COMMUNITY_PORTAL + '/makerdao-scd-faqs/scd-faqs' + '/makerdao',
        'oracles': MAKER_COMMUNITY_PORTAL + faqs_url + '/oracles',
        'risk_management': MAKER_COMMUNITY_PORTAL + '/makerdao-scd-faqs/scd-faqs' + '/risk-management',
        'stability_fee': MAKER_COMMUNITY_PORTAL + faqs_url + '/stability-fee',
        'vault': MAKER_COMMUNITY_PORTAL + faqs_url + '/vault',
        'faqs_overview': '''
Here's all the [FAQs](https://community-development.makerdao.com/makerdao-mcd-faqs/faqs) you can request
> We've got a glossary:  `glossary`
> Dai: `dai faq`
> Dai Savings Rate: `dsr faq`
> Emergency Shutdown: `shutdown faq`
> Governance: `governance faq`
> Liquidation: `liquidation faq`
> MakerDAO: `maker faq`
> Oracles: `oracle faq`
> Risk: `risk faq`
> Stability Fee: `stability fee faq`'''
    },
    'resources': {
        'dev_docs': 'https://developer.makerdao.com',
        'cdp_portal': 'Heads Up! CDPs are now called Vaults and the portal has moved to Oasis\nhttps://oasis.app/',
        'oasis_app': 'https://oasis.app/borrow',
        'oasis_save': 'https://oasis.app/save',
        'oasis_trade': 'https://oasis.app/trade',
        'governance_dashboard': 'https://vote.makerdao.com',
        'awesome_makerdao': 'https://awesome.makerdao.com',
        'awesome_channels': 'https://awesome.makerdao.com#official-channels',
        'awesome_spend_dai': 'https://awesome.makerdao.com#spend-your-dai',
        'awesome_use_dai': 'https://awesome.makerdao.com#use-your-dai',
        'awesome_lend_dai': 'https://awesome.makerdao.com#lend-your-dai',
        'awesome_watch_dai': 'https://awesome.makerdao.com#watch-your-dai',
        'awesome_hold_dai': 'https://awesome.makerdao.com#hold-your-dai',
        'awesome_trade_dai': 'https://awesome.makerdao.com#trade-your-dai',
        'awesome_dev_resoures': 'https://awesome.makerdao.com#developer-resources',
        'awesome_audits_security': 'https://awesome.makerdao.com#audits-and-security',
        'awesome_overview': '''
Here are the [AMD](https://awesome.makerdao.com) Resources you can request
> Official Channels: `amd channels`
> Spend Dai: `amd spend`
> Use Dai: `amd use`
> Lend Dai: `amd lend`
> Watch Dai: `amd watch`
> Hold Dai: `amd hodl`
> Trade Dai: `amd trade`
> Developer Resources: `amd dev`
> Audits & Security: `amd audit`'''
    },
    'lost': {
        'help': '''
Hey, I'm @mkr.bot. I can help you find resources or information about the Maker Protocol.
> *Commands*
> FAQs: `faqs {{governance | vaults | dai | stability fee}}`
> Spells Count: `spells count`
> Vault Lookup: `vault {{ID}}`
> Awesome MakerDAO: `amd {{use | lend dai | spend | watch dai}}`
[mkr.bot Guide]({mkrbot_guide}) | [Expand my commands!]({contributing_link}) | Let [@scottrepreneur]({creator_dm}) know if you have any issues'''.format(
            mkrbot_guide=MKRBOT_GUIDE_URL,
            contributing_link=CONTRIBUTING_URL,
            creator_dm=CREATOR_DM_URL),
        'no_commands': '''
I didn\'t get you. Let me look up those Maker resources for you.
> *Commands*
> FAQs: `faqs {{governance | vaults | dai | stability fee}}`
> Spells Count: `spells count`
> Vault Lookup: `vault {{ID}}`
> Awesome MakerDAO: `amd {{use | lend dai | spend | watch dai}}`
[mkr.bot Guide]({mkrbot_guide}) | [Expand my commands!]({contributing_link}) | Let [@scottrepreneur]({creator_dm}) know if you have any issues'''.format(
            mkrbot_guide=MKRBOT_GUIDE_URL,
            contributing_link=CONTRIBUTING_URL,
            creator_dm=CREATOR_DM_URL)
    }
}

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
                if trigger_group != 'queries':
                    for sub in mkrbot_triggers[trigger_group][query]:

                        # match any case
                        if message.casefold() == sub.casefold():
                            command_found = True
                            bot_response(user, mkrbot_responses[trigger_group][query], channel, True)

                # handle queries here so regex can be used and pass parameters to functions
                else:
                    for sub in mkrbot_triggers[trigger_group][query]:

                        # depending on the query, regex match
                        if query == 'spell_count':

                            # match any case
                            if message.casefold() == sub.casefold():
                                command_found = True
                                bot_response(user, print_spells(), channel, True)

                        elif query == 'check_vault':
                            if re.compile(sub).match(message):
                                command_found = True
                                bot_response(user, get_vault_by_id(message), channel, True)
        
        # don't send two commands
        if command_found:
            break;
        else:               # otherwise send no commands found
            command_found = True
            bot_response(user, mkrbot_responses['lost']['no_commands'], channel, True)

def bot_response(_user, _message, _channel, unfurl):
    # print only on Dev
    if ENVIRONMENT == 'PRODUCTION':
        if unfurl:
            rocket.send_message(_message, channels['chakachat'])
        else:
            rocket.send_message(_message, channels['chakachat'], parseUrls=False)
    
    else:
        print(_message)
