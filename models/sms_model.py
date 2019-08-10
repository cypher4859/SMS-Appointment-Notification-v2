from sms_v2.models.base_model import base_model

class sms_send_model(base_model):
	account_sid = ""
	auth_token = ""
	recipient = ""
	sender = ""
	message = ""
	callback = ""
