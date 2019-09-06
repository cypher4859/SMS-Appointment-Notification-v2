import pytest
import json
from sms_v2.tests.conftest import client
from sms_v2.tests.json_payloads import json_payloads
from flask import url_for

@pytest.mark.usefixtures('client_class')
class TestClass:

	headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}

	test_payloads = json_payloads()

	def test_hello_world(self):
		assert self.client.get().status_code == 200

	def test_negative_hello_world(self):
		assert self.client.get('/someshit').status_code != 200

	def test_can_grab_json(self):
		assert self.headers == self.test_payloads.headers

	def test_read_all_rows(self):
		assert self.client.get('/read_all_rows').status_code == 200

	def test_get_appointment_status(self):
		assert self.client.get('/get_appointment_status').status_code == 200

	def test_get_message_delivery_status(self):
		assert self.client.get('/get_message_delivery_status').status_code == 200


	#pytest.mark.xfail
	def test_receive_sms_reply(self):
		assert self.client.post('/receive_sms_reply', data=json.dumps(self.test_payloads.test_receive_sms_reply_json_payload), headers=self.headers).status_code == 204


	@pytest.mark.skip
	def test_receive_message_status(self):
		assert self.client.post('/receive_message_status', data=json.dumps(self.test_payloads.test_receive_sms_status_json_payload), headers=self.headers).status_code == 204

	@pytest.mark.skip
	def test_notify_appointments(self):
		assert self.client.post('/notify_appointments', data=json.dumps(self.test_payloads.test_notify_json_payload), headers=self.headers).status_code == 204
 
