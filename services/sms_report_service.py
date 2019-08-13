import ipdb as pdb
import json
from twilio.rest import Client
from sms_v2.utilities import dev as util

class report:
	def __init__(self, message="", patient="", doctor_office_number="", message_sid="", message_stat=""):
		self.sid = message_sid
		self.deliv_stat = message_stat
		self.patient = patient
		self.doctor_office_number = doctor_office_number
		self.message = message

	def report_delivery_status(self, sid, stat):
		#pdb.set_trace()
		# UPDATE DB
		# Find Row with MessageSid, Update its delivery status
		util.update_message_delivery_status(sid, stat)

	def report_appointment_status(self, patient, message, doctor_office_number):
		patient = patient[2:]
		office_phone_number = doctor_office_number[2:]
		reply = message

		#import ipdb; ipbd.set_trace()
		is_valid_response, confirmation = self.validate_reply(reply)
		if(is_valid_response):
			#update with Confirmed
			util.confirm_appt_status(patient, office_phone_number, confirmation)


	def validate_reply(self, reply):
		if(reply == "Y"):
			return True, "Confirmed"
		elif(reply == "N"):
			return True, "Cancelled"
		else:
			return False, ""
