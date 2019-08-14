import json
from twilio.rest import Client
from sms_v2.utilities import dev as util
from .vault_request_service import vault_request
from jsonschema import validate

class sms:
	def __init__(self, payload):
		self.json_payload = payload

	def load(self):
		try:
			isValid = self.validate_payload(self.json_payload)
			try:
				#self.load_request_receipt_into_database()
				for index, message in enumerate(self.json_payload):
					self.send(message)
					print("Successfully Sent!")
				return index+1
			except:
				print("Couldn't Send")
		except:
			print("Couldn't sanitize")
			return

	def validate_payload(self, payload):
		#return False
		#check the input
		#test JSON aginst schema
		schema = {
			"type" : "array",
			"items": {
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
						}
					},
					"doctor" : {"type" : "string"},
					"message" : {"type" : "string"},
					"doctor_office" : {"type" : "string"},
					"doctor_number" : {"type" : "string"},
					"acct" : {"type" : "string"},
					"token" : {"type" : "string"},
					"secret_name" : {"type" : "string"},
					"delivery_status" : {"type" : "string"}
				}
			},
		}
		try:
			validate(payload, schema=schema)
			return True
		except:
			return False

	def send(self, package):
		#twilio python sender
		# Get account data
		secret_name = package['secret_name']

		v = vault_request(secret_name)
		if(package['acct'] == v.request_sid()):
			package['token'] = v.request_token()
		
		client = Client(package['acct'], package['token'])
		#import ipdb as pdb; pdb.set_trace()
		#print("Make sure to set the correct ngrok status_callback URL\n ngrok http 5000")
		message = client.messages.create(
			to="+1"+package['patient_number'],
			from_="+1"+package['doctor_number'],
			body=package['message'],
			status_callback="https://512daef5.ngrok.io/receive_message_status")

		package['message_sid'] = message.sid

		self.load_message_into_database(package)

	def load_message_into_database(self, package):
		util.insert_one_appointment(package)
