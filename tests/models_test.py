from sms_v2.models.receive_message_model import receive_message_model


class TestClass:
	def test_receive_message_model(self):
		test_package = {
			'from': '',
			'body': '',
			'to': '',
			'sid': '',
			'error_code': '',
			'error_message': '',
			'num_media': '',
			'num_segments': '',
			'price': '',
			'price_unit': '',
			'uri': '',
			'status': ''
		}

		test_model = receive_message_model(test_package)
		assert type(test_model) is receive_message_model, 'Its not the right model'
