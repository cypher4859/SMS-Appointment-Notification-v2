from sms_v2.models.base_model import base_model

class receive_delivery_status_model(base_model):
	def __init__(self, payload):
		#import ipdb; ipdb.set_trace()
		self.acct = payload['AccountSid']
		self.message_from = payload['From']
		self.message_sid = payload['MessageSid']
		self.delivery_status = payload['MessageStatus']
		self.message_to = payload['To']
