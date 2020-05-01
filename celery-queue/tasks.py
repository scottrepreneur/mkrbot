import os
import time
from celery import Celery
from celery.schedules import crontab

from rocket import approved_channels, channels
from mkrbot import mkrbot_names, mkrbot_triggers, mkrbot_message, bot_response
from reddit import forum_cross_post
from prices import price_update
from gov_updates import check_new_spell, check_cast_spell, check_new_poll

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.scheduled_price_update', bind=True)
def scheduled_price_update(self):
    bot_response('user', price_update(), channels['chakachat'], True)

@celery.task(name='tasks.check_new_spell_task', bind=True)
def check_new_spell_task(self):
    check_new_spell()

@celery.task(name='tasks.check_cast_spell_task', bind=True)
def check_cast_spell_task(self):
    check_cast_spell()

@celery.task(name='tasks.check_new_poll_task', bind=True)
def check_new_poll_task(self):
    check_new_poll()

@celery.task(name='tasks.process_message', bind=True)
def process_message(self, user, message, channel, dm):
	
	# anyone can dm, maybe want to add a blacklist eventually?
	if dm:
		_message = message
		mkrbot_message(user, _message, channel)

	# check for @mkr.bot trigger on channel messages
	else:
		for c in approved_channels:
			print(channels[c] == channel)
			if channel == channels[c]:
				print(message[:message.find(' ')].casefold())
				for name in mkrbot_names:
					if message[:message.find(' ')].casefold() == name.casefold():
						_message = message[message.find(' '):]
						mkrbot_message(user, _message, channel)

@celery.task(name='tasks.forum_update', bind=True)
def forum_update(self, data):
	post = data['post']
	print(post)

	# production forum GaaG, LFW update
	if post['topic_id'] == 84 and post['username'] == 'LongForWisdom' and post['post_number'] != 1:
		print('LFW updating GaaG')
		forum_cross_post(post, False)

	# staging forum GaaG, scottrepreneur update
	elif post['topic_id'] == 15 and post['username'] == 'scott.herren1' and post['post_number'] != 1:
		print('scooter update staging GaaG')
		forum_cross_post(post, True)
	
	else:
		print('not LFW updating GaaG')
