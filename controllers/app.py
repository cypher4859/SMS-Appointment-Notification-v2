#!/usr/bin/python3.7

import json
from flask import Flask
from flask import request
from flask import jsonify
from sms_v2.services.sms_send_service import sms as sms_service_send
from sms_v2.services.sms_report_service import report
from sms_v2.services.sms_receive_service import receive
from sms_v2.utilities.helper_functions import dev

app = Flask(__name__)

@app.route("/")
def hello():
	#pdb.set_trace()
	return "Hello World"

@app.route("/read_all_rows")
def get_rows():
	d = dev()
	x = d.read_all_appointments()
	return jsonify(str(x))



#### Getters
@app.route("/get_appointment_status", methods=['GET'])
def get_appt_confirm_status():
	'''NOTE:
	Get the status of all appointments for the client. Optional filter on range.'''
	pass

@app.route("/get_message_delivery_status", methods=['GET'])
def get_message_deliv_status():
	'''Get the delivery status of all the messages sent out. Optional Filter on range.'''
	pass






####Setters
@app.route("/receive_message_status", methods=['POST'])
def receive_message_status():
	#if request.method == 'POST':
		# To test!

	#	message_sid = request.values.get('MessageSid', None)
	#	message_status = request.values.get('MessageStatus', None)
	#	message_acct = request.values.get('AccountSid', None)

	#	receiver = receive()
	#	receiver.record_status(message_sid, message_status, message_acct)

	#	return ('', 204)

	#if request.method == 'POST':
	#	import ipdb; ipdb.set_trace()
	#	receiver = receive(request.json['FormValues'])
	#	receiver.record_status()
	
	if(request.method == 'POST'):
		import ipdb; ipdb.set_trace()
		reporter = report(request.json['FormValues'])
		reporter.reporter_delivery_status

		return ('', 204)


@app.route("/receive_sms_reply", methods=['POST'])
def receive_sms_reply():
	#if request.method == 'POST':
	#	message_from = request.json['from']
	#	body = request.json['body']
	#	message_to = request.json['to']
	#	message_acct = request.json['account_sid']

	#	receiver = receive()
	#	receiver.record_response(message_from, body, message_to, message_acct)
	#	return ('', 204)



	if request.method == 'POST':
		receiver = receive(request.json)
		receiver.record_response()
		return ('', 204)



## Doers
@app.route("/notify_appointments", methods=['POST'])
def upload_appts():
	results = []
	if request.method == 'POST':
		collection_of_messages_to_send = request.json
		try:
			sms_sender = sms_service_send(collection_of_messages_to_send)
			res = sms_sender.load()
			results.append(res)
		except:
			results.append("Could not upload the message data!")

		final_result = "fuckk"
		return ('', 204)


if(__name__ == '__main__'):
    app.run(host="0.0.0.0", debug=True)
