import json
from twilio.rest import Client
from sms_v2.utilities import dev as util

class report:
	def __init__(self, message, patient="", doctor_office_number="", message_sid="", message_stat=""):
		self.sid = message_sid
		self.deliv_stat = message_stat
		self.patient = patient
		self.doctor_office_number = doctor_office_number
		self.message = message

	def report_devliery_status(self):
		sid = self.sid
		stat = self.deliv_stat

		# UPDATE DB
		# Find Row with MessageSid, Update its delivery status

	def report_appointment_status(self):
		patient = self.patient[2:]
		office_phone_number = self.doctor_office_number[2:]
		reply = self.message

		#import ipdb; ipbd.set_trace()
		is_valid_response, confirmation = self.validate_reply(reply)
		if(is_valid_response):
			#update with Confirmed
			util.confirm_appt_status(patient, office_phone_number, confirmation)


			# Update DB
			# Find appointment that has `patient` number and `office_phone_number`
			# Set appointment status to `Confirmed` or `Cancelled`
			

		#else:
			#pass
			# respond negatively? 

	def validate_reply(self, reply):
		if(reply == "Y"):
			return True, "Confirmed"
		elif(reply == "N"):
			return True, "Cancelled"
		else:
			return False, ""
