
import os
from rocketchat.api import RocketChatAPI

MAKER_CHAT_DOMAIN = os.getenv('MAKER_CHAT_DOMAIN')
ROCKET_BOT_USER = os.getenv('ROCKET_BOT_USER')
ROCKET_BOT_PASSWORD = os.getenv('ROCKET_BOT_PASSWORD')

channels = {
	# bots ONLY!
	'chakachat': '2oLA6ctJWzi43YAKW',
	# If general/random/speculation allowed
	'general': 'GENERAL',
	'governance_and_risk': 'LupC4xAn8JC4CHBbE',
	'random': 'HYo67E5fbCPgsW5pT',
	'speculation': 'snxzQpA4m9CjB2T2v'
}

rocket = RocketChatAPI(settings={
	'username': ROCKET_BOT_USER, 
	'password': ROCKET_BOT_PASSWORD,
 	'domain': MAKER_CHAT_DOMAIN
 	})
