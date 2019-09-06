#This should test that the app controller does what its supposed to do
import pytest
from sms_v2.controllers.app import app

@pytest.fixture
def client():
	yield app.test_client()
