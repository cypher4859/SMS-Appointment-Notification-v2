import json
from twilio.rest import Client
from sms_v2.services.sms_report_service import report
from sms_v2.models.receive_message_model import receive_message_model
from sms_v2.models.receive_delivery_status_model import receive_delivery_status_model

class receive:
	def __init__(self, receive_model):
		if(type(receive_model) is receive_message_model):
			self.fro = receive_model.message_from
			self.body = receive_model.message_body
			self.to = receive_model.message_to
			self.acct = receive_model.acct

		elif(type(receive_model) is receive_delivery_status_model):
			self.sms_sid = receive_model.message_sid
			self.status = receive_model.delivery_status
			self.acct = receive_model.acct

	def record_response(self):
		#import ipdb; ipdb.set_trace()
		reporter = report()
		reporter.report_appointment_status(self.fro, self.body, self.to, self.acct)

	def record_status(self):
		reporter_payload = { 
			'message_body': '', 
			'delivery_status': self.status,
			'message_sid': self.sms_sid,
			'acct': self.acct,
			'message_to': '', 
			'message_from': ''
		}

		reporter = report(reporter_payload)
		reporter.report_delivery_status()
