import json
from twilio.rest import Client
from sms_v2.utilities import dev as util
from sms_v2.utilities.helper_functions import dev
from sms_v2.models.receive_message_model import receive_message_model
from sms_v2.models.receive_delivery_status_model import receive_delivery_status_model

class report:
	def __init__(self, payload):
		if(type(payload) is receive_delivery_status_model):
			self.sms_sid = payload.message_sid
			self.status = payload.delivery_status
			self.acct = payload.acct

		elif(type(payload) is receive_message_model):
			self.fro = payload.message_from
			self.body = payload.message_body
			self.to = payload.message_to
			self.acct = payload.acct


	def report_delivery_status(self):
		#pdb.set_trace()
		# UPDATE DB
		# Find Row with MessageSid, Update its delivery status
		d = dev()
		d.update_message_delivery_status(self.sms_sid, self.status, self.acct)

	def report_appointment_status(self):
		patient_number = self.fro[2:]
		office_phone_number = self.to[2:]
		reply = self.body
		acct = self.acct

		is_valid_response, confirmation = self.validate_reply()
		if(is_valid_response):
			#update with Confirmed
			d = dev()
			d.confirm_appt_status(patient_number, office_phone_number, confirmation, acct)



	def validate_reply(self):
		reply = self.body

		if(reply == "Y"):
			return True, "Confirmed"
		elif(reply == "N"):
			return True, "Cancelled"
		else:
			return False, ""
