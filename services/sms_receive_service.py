import json
from twilio.rest import Client
from sms_v2.utilities import dev as util
from sms_v2.services.sms_report_service import report

class receive:
	def __init__(self, message_from="", message_body="", message_to="", message_acct=""):
		self.fro = message_from
		self.body = message_body
		self.to = message_to
		self.acct = message_acct

	def record_response(self, fro, body, to):
		#import ipdb; ipdb.set_trace()
		reporter = report()
		reporter.report_appointment_status(fro, body, to)

	def record_status(self, sid, status, acct):
		reporter = report()
		reporter.report_delivery_status(sid, status, acct)
