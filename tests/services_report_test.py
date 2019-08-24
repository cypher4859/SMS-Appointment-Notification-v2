# This should test that the reporter service does what its supposed to do

from sms_v2.services.sms_report_service import report
from sms_v2.models.receive_message_model import receive_message_model
from sms_v2.models.receive_delivery_status_model import receive_delivery_status_model

class TestClass:
	def test_deliv_status_initialization(self):
		deliv_model = {
			'AccountSid': '',
			'From': '',
			'MessageSid': '',
			'MessageStatus': '',
			'To': ''
		}

		payload = receive_delivery_status_model(deliv_model)

		reporter = report(payload)
		assert reporter.sms_sid is not None, 'sms_sid is Null'
		assert reporter.status is not None, 'status is Null'
		assert reporter.acct is not None, 'acct is Null'

	def test_receive_message_initialization(self):
		message_model = {
			'from': '',
			'body': '',
			'to': '',
			'account_sid': '',
			'error_code': '',
			'error_message': '',
			'num_media': '',
			'num_segments': '',
			'price': '',
			'price_unit': '',
			'uri': '',
			'status': ''
		}

		payload = receive_message_model(message_model)

		reporter = report(payload)
		assert reporter.fro is not None, 'reporter.fro is null'
		assert reporter.body is not None, 'reporter.body is null'
		assert reporter.to is not None, 'reporter.to is null'
		assert reporter.acct is not None, 'reporter.acct is null'

	def test_validate_reply(self):
		message_model = {
			'from': '',
			'body': '',
			'to': '',
			'account_sid': '',
			'error_code': '',
			'error_message': '',
			'num_media': '',
			'num_segments': '',
			'price': '',
			'price_unit': '',
			'uri': '',
			'status': ''
		}

		payload = receive_message_model(message_model)

		reporter = report(payload)
		assert reporter.validate_reply() == (False, ''), 'Could not validate on default empty message'

		reporter.body = 'Y'
		assert reporter.validate_reply() == (True, 'Confirmed'), 'Could not validate a message of Y'

		reporter.body = 'N'
		assert reporter.validate_reply() == (True, 'Cancelled'), 'Could not validate a message of N'
