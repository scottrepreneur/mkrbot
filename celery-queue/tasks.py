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
def process_message(self, user, message, channel):
	
	# TODO handle DM here
	if not 'bot' in message[:message.find(' ')]:
		_message = message

	# check for @mkr.bot trigger
	for channel in approved_channels:
		if channel == channels[channel]:
			print(message[:message.find(' ')].casefold())
			for name in mkrbot_names:
				if message[:message.find(' ')].casefold() == name.casefold():
					_message = message[message.find(' '):]
	
	mkrbot_message(user, _message, channel)

@celery.task(name='tasks.forum_update', bind=True)
def forum_update(self, data):

	if data['topic_id'] == 84 and data['username'] == 'LongForWisdom':
		forum_cross_post(data)
