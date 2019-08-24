
from sms_v2.utilities.helper_functions import dev

class TestClass:
	def test_insert_one_appointment(self):
		payload = {
			'x': 'ahhhhh'
		}
		d = dev()
		d.insert_one_appointment(payload)

		assert d.insert_one_appointment(payload) == None, 'it fucked up'

	#def test_
