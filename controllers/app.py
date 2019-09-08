#!/usr/bin/python3.7

import time
import json
from flask import Flask
from flask import request
from flask import jsonify
from sms_v2.services.distribute_service import distributor
from sms_v2.services.sms_report_service import report
from sms_v2.utilities.helper_functions import dev
from sms_v2.models.receive_message_model import receive_message_model
from sms_v2.models.receive_delivery_status_model import receive_delivery_status_model

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
	return ('', 200)

@app.route("/get_message_delivery_status", methods=['GET'])
def get_message_deliv_status():
	'''Get the delivery status of all the messages sent out. Optional Filter on range.'''
	return ('', 200)






####Setters
@app.route("/receive_message_status", methods=['POST'])
def receive_message_status():
	if(request.method == 'POST'):
		deliv_model = receive_delivery_status_model(request.values)
		reporter = report(deliv_model)
		reporter.report_delivery_status()

		return ('', 204)


@app.route("/receive_sms_reply", methods=['POST'])
def receive_sms_reply():
	if request.method == 'POST':
		message_model = receive_message_model(request.json)
		reporter = report(message_model)
		reporter.report_appointment_status()
		return ('', 204)



## Doers
@app.route("/schedule_notify_appointments", methods=['POST'])
def schedule_upload_appts():
	if(request.method == 'POST'):
		collection_of_messages = request.json
		distribute = distributor(collection_of_messages)
		distribute.distribute_to_scheduler()

		return ('', 204)		


@app.route("/notify_appointments", methods=['POST'])
def upload_appts():
	results = []
	if request.method == 'POST':
		collection_of_messages_to_send = request.json
		distribute = distributor(collection_of_messages_to_send)
		distribute.distribute_to_sender()

		return ('', 204)


if(__name__ == '__main__'):
    app.run(host="0.0.0.0", debug=True)
