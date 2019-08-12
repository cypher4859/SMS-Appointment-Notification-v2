import json
from twilio.rest import Client
from sms_v2.utilities import dev as util
from sms_v2.services.sms_report_service import report

class receive:
	def __init__(self, message_from="", message_body="", message_to=""):
		self.fro = message_from
		self.body = message_body
		self.to = message_to

	def record_response(self):
		#import ipdb; ipdb.set_trace()
		reporter = report(self.body, self.fro, self.to)
		reporter.report_appointment_status()

	def record_status(self, sid, status):
		reporter = report()
		reporter.report_delivery_status(sid, status)
