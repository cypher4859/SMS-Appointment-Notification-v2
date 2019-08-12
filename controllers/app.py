#!/usr/bin/python3.7

import json
import ipdb as pdb
from flask import Flask
from flask import request
from flask import jsonify
from sms_v2.services.sms_send_service import sms as sms_service_send
from sms_v2.services.sms_report_service import report
from sms_v2.services.sms_receive_service import receive
from sms_v2.utilities import dev as util


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("/read_all_rows")
def get_rows():
	x = util.read_all_appointments()
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
	if request.method == 'POST':
		message_sid = request.json['MessageSid']
		message_status = request.json['MessageStatus']
		

		#pdb.set_trace()
		receiver = receive()
		receiver.record_status(message_sid, message_status)

		return ('', 204)


@app.route("/receive_sms_reply", methods=['POST'])
def receive_sms_reply():
	if request.method == 'POST':
		message_from = request.json['from']
		body = request.json['body']
		message_to = request.json['to']

		#import ipdb; ipdb.set_trace()
		receiver = receive(message_from, body, message_to)
		receiver.record_response()
		return ('', 204)






## Doers
@app.route("/notify_appointments", methods=['POST'])
def upload_appts():
	results = []
	if request.method == 'POST':
		#import ipdb as pdb; pdb.set_trace()
		payload = request.json
		try:
			sms_sender = sms_service_send(payload)
			res = sms_sender.load()
			results.append(res)
		except:
			results.append("Could not upload the message data!")

		final_result = "fuckk"
		return ('', 204)


if(__name__ == '__main__'):
    app.run(host="0.0.0.0", debug=True)
