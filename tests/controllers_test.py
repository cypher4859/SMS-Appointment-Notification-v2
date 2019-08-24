#This should test that the app controller does what its supposed to do
import pytest
from sms_v2.controllers import app

class controller_test:
	def test_hello(self):
		assert app.hello() == "Hello World"

	'''def hello(self):
		return "Hello World"'''
