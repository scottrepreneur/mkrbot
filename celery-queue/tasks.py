import os
import time
from celery import Celery

from rocket import approved_channels, channels
from mkrbot import mkrbot_names, mkrbot_triggers, mkrbot_message
from reddit import forum_cross_post

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y

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

	if post['topic_id'] == 84 and post['username'] == 'LongForWisdom' and post['post_number'] != 1:
		forum_cross_post(post)
	
	else:
		print('not LFW updating GaaG')
