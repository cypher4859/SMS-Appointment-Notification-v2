from sms_v2.models.base_model import base_model

class receive_message_model(base_model):
	def __init__(self, payload):
		self.message_from = payload['from']
		self.message_body = payload['body']
		self.message_to = payload['to']
		self.acct = payload['account_sid']
		self.error_code = payload['error_code']
		self.error_message = payload['error_message']
		self.num_media = payload['num_media']
		self.num_segments = payload['num_segments']
		self.price = payload['price']
		self.price_unit = payload['price_unit']
		self.message_uri = payload['uri']
		self.status = payload['status']
