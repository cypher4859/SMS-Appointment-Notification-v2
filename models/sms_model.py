from datetime import datetime
from sms_v2.models.base_model import base_model
from sms_v2.services.vault_request_service import vault_request

class sms_send_model(base_model):
	def __init__(self, payload):
		# Initialize the instance
		self.chart = payload['chart']
		self.patient_number = payload['patient_number']
		self.name = payload['name']
		self.date_created = payload['date_created']
		self.appointment = { 'date' : payload['appointment']['date'], 'time' : payload['appointment']['time'], 'status' : payload['appointment']['status'], 'fulldate' : '', 'timezone': payload['appointment']['timezone']}
		self.doctor = payload['doctor']
		self.message = payload['message']
		self.doctor_office = payload['doctor_office']
		self.doctor_number = payload['doctor_number']
		self.acct = payload['acct']
		self.token = payload['token']
		self.secret_name = payload['secret_name']
		self.delivery_status = payload['delivery_status']
		self.message_sid = ''
		self.scheduled_time = payload['scheduled_time']
