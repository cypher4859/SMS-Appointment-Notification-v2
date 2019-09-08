# This should test that the send service does what its supposed to do

from sms_v2.services.sms_send_service import sms
from sms_v2.transformers.date_transformer import date as da
from sms_v2.tests.json_payloads import json_payloads as test_json

import pytest

class TestClass:
	#####
	# Not testing load() or send() right now because I don't want it to fire off the message
	# everytime I run pytest.
	# I can however test parts of it, like basically everything except self.send()

	#@pytest.mark.xfail
	def test_load(self):
		#This assumes that self.send() and load_message_info_database() are commented out
		payload = test_json()
		test_object = sms(payload.test_notify_json_payload[0])
		assert test_object.load() is None


	#@pytest.mark.xfail
	def test_negative_load(self):
		payload = test_json()
		test_obj = sms(payload.test_negative_sms_sender_json_payload)
		with pytest.raises(AssertionError):
			assert test_obj.load is None


	#@pytest.mark.xfail
	def test_validate_payload(self):
		payload = test_json()
		test_object = sms(payload.test_notify_json_payload[0])
		assert test_object.validate_payload() is True

	def test_get_vault_data(self):
		p = None
		test_object = sms(p)

		secret = 'childerstaylor'
		sid = 'AC471e900502c9d036fa8cc7e6a50682e9'

		assert test_object.get_vault_data(secret, sid) == 'be7031685eb85221bcd00917b377db48'

	# It would be tedious to test the get utc appointment date function because of exact millisecond
	# def test_get_utc_appointment_date():
	
	def test_get_date_created(self):
		p = {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": ""
		}
		date_object = da(p)
		test_object = sms(p)
		assert test_object.get_utc_appointment_date(p) == date_object.transform_get_full_date()
