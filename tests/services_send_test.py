# This should test that the send service does what its supposed to do

from sms_v2.services.sms_send_service import sms
from sms_v2.transformers.date_transformer import date as da

class TestClass:
	#####
	# Not testing load() or send() right now because I don't want it to fire off the message
	# everytime I run pytest.
	# I can however test parts of it, like basically everything except self.send()

	def test_validate_payload(self):
		payload = [{
			"chart": "someChart",
			"patient_number": "3044446329",
			"name": "testting",
			"date_created": "",
			"appointment": {
				"date": "2019-08-20",
				"time": "1:06pm",
				"status": "Unconfirmed",
				"timezone": ""
			},
			"doctor": "Dr. Strange",
			"message": "Test new system",
			"doctor_office": "The Office",
			"doctor_number": "3047605956",
			"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
			"token": "",
			"secret_name": "childerstaylor",
			"delivery_status": "",
			"scheduled_time": ""
		}]


		test_object = sms(payload)
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
