import pytest
import pytz
from datetime import datetime
from sms_v2.transformers.date_transformer import date
from sms_v2.transformers.generic_date_transformer import generic_date

class TestClass:
	def get_valid_model(self):
		return { 
			'date': '2019-09-10',
			'time': '6:53pm',
			'status': 'Unconfirmed',
			'timezone': 'US/Eastern'
		}


	def test_transform_get_full_date(self):
		transformer = date(self.get_valid_model())
		expected_json = { 
			'date': datetime(2019, 9, 10, 0, 0), 
			'time': datetime(1900, 1, 1, 18, 53), 
			'status': 'Unconfirmed',
			'fulldate': datetime(2019, 9, 10, 18, 53),
			'timezone': 'US/Eastern'
		}
		assert transformer.transform_get_full_date() == expected_json

	def test_transform_generic_date(self):
		transformer = generic_date(self.get_valid_model())
		obj = datetime(2019, 9, 10, 18, 53, tzinfo=pytz.utc)
		assert transformer.transform_into_datetime_object() == obj
