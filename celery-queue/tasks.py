import os
import time
from celery import Celery

from mkrbot import mkrbot_triggers, mkrbot_message

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y

@celery.task(name='tasks.process_message', bind=True)
def process_message(self, user, message, channel):
	# check for @mkr.bot trigger
	if message.split(' ')[0] in mkrbot_triggers['names']:
		_message = message[message.find(message.split(' ')[1]):]
		mkrbot_message(user, _message, channel)
