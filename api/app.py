import os
import json
from flask import Flask, request, jsonify
from flask import url_for
from worker import celery
import celery.states as states

app = Flask(__name__)

MKRBOT_TOKEN = os.getenv('MKRBOT_TOKEN')

@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
	task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
	response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
	return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
	res = celery.AsyncResult(task_id)
	if res.state == states.PENDING:
		return res.state
	else:
		return str(res.result)

@app.route('/webhook', methods=['GET', 'POST'])
def maker_chat():
	if request.method == 'GET':
		verify_token = request.args.get('verify_token')
		if verify_token == MKRBOT_TOKEN:
			authorised_clients[request.remote_addr] = datetime.now()
			return jsonify({'status':'success'}), 200
		else:
			return jsonify({'status':'bad token'}), 401

	elif request.method == 'POST':

		verify_token = request.headers.get('verify_token')
		if verify_token == MKRBOT_TOKEN:
			# print(request.data)
			if request.data:
				data = json.loads(request.data)
				print(data)
				user = data['user']
				message = data['message']
				channel = data['channel']
				
				message = celery.send_task('tasks.process_message', args=[user, message, channel], kwargs={})
				# message = process_message.delay(user, message, channel)

				return jsonify({'status':'success'}), 200
			
			else:
				return jsonify({'status':'no data in webhook'}), 400

		else:
			return jsonify({'status':'not authorised'}), 401

	else:
		return jsonify({'status':'success'}), 400
