import os
import re
from rocket import channels, rocket

from check_hat import check_spells
from cdp import get_cdp_by_id

MAKER_COMMUNITY_PORTAL = os.getenv('MAKER_COMMUNITY_PORTAL')

# TODO Add MKR Burn makerburn.com

mkrbot_triggers = {
	'names': [
		'@mkr.bot',
		'@mkrbot',
        'mkr.bot',
		'mkrbot',
        'bot'
	],
	'spell_count': [
		'spell count',
        'spells count',
		'chief spells',
		'chief spells count',
		'chief spell count',
		'What is the spell count',
		'mkr on spells',
        'mkr on spell',
		'mkr per spells',
        'mkr per spell'
	],
    'check_cdp':[
        'cdp [0-9]',
        'vault [0-9]'
    ],
    'faqs': {
        'cdp': [
            'faqs cdp',
            'faq cdp',
            'cdp faqs',
            'cdp faq',
            'what is a cdp',
            'what is cdp',
            'what is a cdp?',
            'faqs vaults',
            'faq vaults',
            'vault faqs',
            'vault faq',
            'what is a vault',
            'what is a vault?'
        ],
        'dai': [
            'faqs dai',
            'faq dai',
            'dai faqs',
            'dai faq',
            'what is dai',
            'what is dai?'
        ],
        'emergency_shutdown': [
            'faqs shutdown',
            'faq emergency shutdown',
            'shutdown faqs',
            'shutdown faq',
            'emergency shutdown faqs',
            'emergency shutdown faq',
            'what is emergency shutdown',
            'what is emergency shutdown?'
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
            'what is a keeper?'
        ],
        'liquidation': [
            'faqs liquidation',
            'faq liquidation',
            'liquidation faqs',
            'liquidation faq',
            'what is liquidation'
            'what is liquidation?'
        ],
        'makerdao': [
            'faqs maker',
            'faq maker',
            'maker faqs',
            'maker faq',
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
            'what is risk',
            'what is risk?',
            'what is risk management',
            'what is risk management?'
        ],
        'stability_fee': [
            'faqs stability',
            'faq stability',
            'stability faqs',
            'stability fee faqs',
            'stability faq',
            'stability fee faq',
            'what is the stability fee',
            'what is the stability fee?'
        ]
    },
    'resources': {
        'cdp_portal': [
            'cdp portal',
            'cdps portal',
            'portal cdp'
        ],
        'governance_dashboard': [
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
            'awesome dev resource'
            'awesome developer',
            'awesome developer resources',
            'awesome developer resource',
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
    }
}

language_code = '/en'
faqs_url = '/faqs'
mkrbot_responses = {
    'faqs': {
        'cdp': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/cdp',
        'dai': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/dai',
        'emergency_shutdown': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/emergency-shutdown',
        'governance': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/governance',
        'keepers': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/keepers',
        'liquidation': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/liquidation',
        'makerdao': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/makerdao',
        'oracles': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/oracles',
        'risk_management': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/risk-management',
        'stability_fee': MAKER_COMMUNITY_PORTAL + language_code + faqs_url + '/stability-fee',
    },
    'resources': {
        'cdp_portal': 'https://cdp.makerdao.com',
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
    },
    'help': '''Commands Available:
        FAQs: `faqs {governance}`
        Spells Count: `spells count`
        CDP Lookup: `cdp {ID}`
        Awesome MakerDAO `amd {section}`'''
}

def mkrbot_message(user, message, channel):
    print(message)

    #* fetch system metrics
    if message in mkrbot_triggers['spell_count']:
        bot_response(user, check_spells(), channel)
    elif re.compile(mkrbot_triggers['check_cdp'][0]).match(message):
        bot_response(user, get_cdp_by_id(message), channel)

    #* faqs commands
    elif message in mkrbot_triggers['faqs']['cdp']:
        bot_response(user, mkrbot_responses['faqs']['cdp'], channel)
    elif message in mkrbot_triggers['faqs']['dai']:
        bot_response(user, mkrbot_responses['faqs']['dai'], channel)
    elif message in mkrbot_triggers['faqs']['emergency_shutdown']:
        bot_response(user, mkrbot_responses['faqs']['emergency_shutdown'], channel)
    elif message in mkrbot_triggers['faqs']['keepers']:
        bot_response(user, mkrbot_responses['faqs']['keepers'], channel)
    elif message in mkrbot_triggers['faqs']['governance']:
        bot_response(user, mkrbot_responses['faqs']['governance'], channel)
    elif message in mkrbot_triggers['faqs']['liquidation']:
        bot_response(user, mkrbot_responses['faqs']['liquidation'], channel)
    elif message in mkrbot_triggers['faqs']['makerdao']:
        bot_response(user, mkrbot_responses['faqs']['makerdao'], channel)
    elif message in mkrbot_triggers['faqs']['oracles']:
        bot_response(user, mkrbot_responses['faqs']['oracles'], channel)
    elif message in mkrbot_triggers['faqs']['risk_management']:
        bot_response(user, mkrbot_responses['faqs']['risk_management'], channel)
    elif message in mkrbot_triggers['faqs']['stability_fee']:
        bot_response(user, mkrbot_responses['faqs']['stability_fee'], channel)
    
    #* resources commands
    elif message in mkrbot_triggers['resources']['cdp_portal']:
        bot_response(user, mkrbot_responses['resources']['cdp_portal'], channel)
    elif message in mkrbot_triggers['resources']['governance_dashboard']:
        bot_response(user, mkrbot_responses['resources']['governance_dashboard'], channel)
    elif message in mkrbot_triggers['resources']['awesome_makerdao']:
        bot_response(user, mkrbot_responses['resources']['awesome_makerdao'], channel)
    elif message in mkrbot_triggers['resources']['awesome_channels']:
        bot_response(user, mkrbot_responses['resources']['awesome_channels'], channel)
    elif message in mkrbot_triggers['resources']['awesome_spend_dai']:
        bot_response(user, mkrbot_responses['resources']['awesome_spend_dai'], channel)
    elif message in mkrbot_triggers['resources']['awesome_use_dai']:
        bot_response(user, mkrbot_responses['resources']['awesome_use_dai'], channel)
    elif message in mkrbot_triggers['resources']['awesome_lend_dai']:
        bot_response(user, mkrbot_responses['resources']['awesome_lend_dai'], channel)
    elif message in mkrbot_triggers['resources']['awesome_watch_dai']:
        bot_response(user, mkrbot_responses['resources']['awesome_watch_dai'], channel)
    elif message in mkrbot_triggers['resources']['awesome_hold_dai']:
        bot_response(user, mkrbot_responses['resources']['awesome_hold_dai'], channel)
    elif message in mkrbot_triggers['resources']['awesome_trade_dai']:
        bot_response(user, mkrbot_responses['resources']['awesome_trade_dai'], channel)
    elif message in mkrbot_triggers['resources']['awesome_dev_resoures']:
        bot_response(user, mkrbot_responses['resources']['awesome_dev_resoures'], channel)
    elif message in mkrbot_triggers['resources']['awesome_audits_security']:
        bot_response(user, mkrbot_responses['resources']['awesome_audits_security'], channel)

    #* help
    elif 'help' in message:
        bot_response(user, mkrbot_responses['help'], channel)
    
    #* default response
    else:
        bot_response(user, 'I didn\'t get you. Try `help` if you need the available commands', channel)


def bot_response(_user, _message, _channel): 
	# print(_message)
	rocket.send_message(_message, channels['chakachat'])
