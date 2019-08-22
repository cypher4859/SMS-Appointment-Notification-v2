from sms_v2.models.base_model import base_model

class receive_delivery_status_model(base_model):
	def __init__(self, payload):
		self.acct = payload['AccountSid'][0]
		self.message_from = payload['MessageFrom'][0]
		self.message_sid = payload['MessageSid'][0]
		self.delivery_status = payload['MessageStatus'][0]
		self.message_to = payload['To'][0]
