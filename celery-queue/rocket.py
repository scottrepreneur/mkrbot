
import os
from api import RocketChatAPI

MAKER_CHAT_DOMAIN = os.getenv('MAKER_CHAT_DOMAIN')
ROCKET_BOT_USER = os.getenv('ROCKET_BOT_USER')
ROCKET_BOT_PASSWORD = os.getenv('ROCKET_BOT_PASSWORD')

approved_channels = [
	'chakachat',
	'community-development'
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
	'chakachat': '2oLA6ctJWzi43YAKW'
}

rocket = RocketChatAPI(settings={
	'username': ROCKET_BOT_USER, 
	'password': ROCKET_BOT_PASSWORD,
 	'domain': MAKER_CHAT_DOMAIN
 	})
