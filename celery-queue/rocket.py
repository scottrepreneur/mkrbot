
import os
from api import RocketChatAPI

env = os.getenv('ENVIRONMENT')

MAKER_CHAT_DOMAIN = os.getenv('MAKER_CHAT_DOMAIN')
ROCKET_BOT_USER = os.getenv('ROCKET_BOT_USER')
ROCKET_BOT_PASSWORD = os.getenv('ROCKET_BOT_PASSWORD')

RCTEST_CHAT_DOMAIN = os.getenv('RCTEST_CHAT_DOMAIN')
RCTEST_BOT_USER = os.getenv('RCTEST_BOT_USER')
RCTEST_BOT_PASSWORD = os.getenv('RCTEST_BOT_PASSWORD')

approved_channels = [
	'chakachat',
	'community-development',
	'scottrepreneur'
]

channels = {
	# check allowed_channels for approved posting locations
	'community-development': 'PYdcER5y2BqRN6NBD',
	'dai-buying': 'kd2TThBZaCPKjeEGa',
	'dai-lending': 'uWvSmmuJAGXtNFMoZ',
	'dai-stablecoin-system': '5ZyxsYX94XfbArwXN',
	'general': 'GENERAL',
	'governance_and_risk': 'LupC4xAn8JC4CHBbE',
	'help': 'DGLW5TiocqWwmZk9x',
	'random': 'HYo67E5fbCPgsW5pT',
	'speculation': 'snxzQpA4m9CjB2T2v',
	# bots ONLY!
	'chakachat': '2oLA6ctJWzi43YAKW',

	#? RC TEST channels
	'scottrepreneur': 'dXA3JbeqP9FfWG3Le'
}

if env == 'PRODUCTION':
	rocket = RocketChatAPI(settings={
		'username': ROCKET_BOT_USER, 
		'password': ROCKET_BOT_PASSWORD,
		'domain': MAKER_CHAT_DOMAIN
		})

else:
	rocket = RocketChatAPI(settings={
		'username': RCTEST_BOT_USER, 
		'password': RCTEST_BOT_PASSWORD,
		'domain': RCTEST_CHAT_DOMAIN
		})
