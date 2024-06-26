import json
import jsonpickle
from datetime import datetime
from twilio.rest import Client
from sms_v2.utilities.helper_functions import dev
from sms_v2.models.sms_model import sms_send_model
from sms_v2.services.vault_request_service import vault_request
from sms_v2.transformers.date_transformer import date
from jsonschema import validate

class sms:
	def __init__(self, payload):
		self.json_payload = payload
		self.validate_payload()

	def load(self):
		try:
			isValid = self.validate_payload()
			try:
				sms_model = sms_send_model(self.json_payload)
				sms_model.token = self.get_vault_data(sms_model.secret_name, sms_model.acct)
				sms_model.date_created = self.get_date_created()
				sms_model.appointment = self.get_utc_appointment_date(sms_model.appointment)
				#sms_model.message_sid = self.send(sms_model)

				#self.load_message_into_database(sms_model.__dict__)
				print("Successfully Sent!")
			except:
				print("Couldn't Send")
		except:
			print("Couldn't sanitize")

	def validate_payload(self):
		#return False
		#check the input
		#test JSON aginst schema
		schema = {
			"type": "object",
			"properties" : {
				"chart" : {"type" : "string"},
				"patient_number" : {"type" : "string"},
				"name" : {"type" : "string"},
				"date_created" : {"type" : "string"},
				"appointment" : {
					"type" : "object",
					"properties" : {
						"date" : {"type" : "string"},
						"time" : {"type" : "string"},
						"status" : {"type" : "string"},
						"timezone": {"type" : "string"}
					}
				},
				"doctor" : {"type" : "string"},
				"message" : {"type" : "string"},
				"doctor_office" : {"type" : "string"},
				"doctor_number" : {"type" : "string"},
				"acct" : {"type" : "string"},
				"token" : {"type" : "string"},
				"secret_name" : {"type" : "string"},
				"delivery_status" : {"type" : "string"},
				"schedule_time" : {
					"type" : "object",
					"properties" : {
						"date" : {"type" : "string"},
						"time" : {"type" : "string"},
						"timezone" : {"type" : "string"}
					}
				}
			},
		}
		try:
			validate(self.json_payload, schema=schema)
			return True
		except:
			return False

	def get_vault_data(self, secret, sid):
		v = vault_request(secret)
		if(sid == v.request_sid()):
			return v.request_token()

	def get_date_created(self):
		date = datetime.utcnow()
		return date

	def get_utc_appointment_date(self, mangled_date):
		d = date(mangled_date)
		return d.transform_get_full_date()



	def send(self, sms_object):
		client = Client(sms_object.acct, sms_object.token)
		#print("Make sure to set the correct ngrok status_callback URL\n ngrok http 5000")
		message = client.messages.create(
			to = "+1" + sms_object.patient_number,
			from_ = "+1" + sms_object.doctor_number,
			body = sms_object.message,
			status_callback="https://8c75d017.ngrok.io/receive_message_status")

		return message.sid

	def load_message_into_database(self, package):
		d = dev()
		d.insert_one_appointment(package)
