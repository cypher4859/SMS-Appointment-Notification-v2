from sms_v2.models.schedule_model import sched_model
from sms_v2.transformers.sched_transformer import schedule_transformer
from sms_v2.services.schedule_service import sched_service
from sms_v2.tests.json_payloads import test_schedule_cases_jsons
from datetime import datetime
from pytz import timezone
import pytz
import pytest


class TestClass:

	cases = test_schedule_cases_jsons

	#@pytest.mark.xfail
	def test_time_format_transformation(self):
		# This will take a time like 23:3:4 and transform it to 23:03:04
		base_example = '23:2:4'
		trans = schedule_transformer(base_example)
		transformed_time = trans.transform_time_to_schedule_job_format()


		assert  transformed_time == '23:02:04', 'Cant transform the time correctly. Try again'

	#@pytest.mark.xfail
	def test_should_fail_sched_service_get_utc_schedule_time(self):
		# The schedule model should only ever take in a dict that contains strings.
		# It should never take in a datetime object
		z = sched_model(datetime(2019, 8, 25, 15, 41, 19, 821795, tzinfo=pytz.utc))
		with pytest.raises(AssertionError):
			assert type(z.obj) is dict, 'The schedule model does not contain a dict'	

		x = sched_service(z.obj)
		with pytest.raises(AttributeError):
			assert x.get_schedule_time() == '15:41:19', 'Has no __dict__ property, the schedule model is not of type dict'

	#@pytest.mark.xfail
	def test_sched_service_get_tzaware_time_from_transformed_time(self):
		z = sched_model(datetime(2019, 8, 25, 22, 1, 9, 821795, tzinfo=pytz.utc))
		# This hsould fail since the obj is not a dictionary with strings
		with pytest.raises(AssertionError):
			assert type(z.obj) is dict, 'The schedule model does not contain a dict'

		# Once the obj has a datetime obj then it should be able to get the timezone aware
		# scheduled time.
		x = sched_service(z.obj)
		assert x.get_tz_aware_schedule_time() == z.obj.astimezone(timezone('US/Eastern'))

	def test_updated_distributor_sched_service_get_utc_schedule_time(self):
		z = sched_model(self.cases.case0)
		assert type(z.obj) is dict


		# This should check that service can get the correct schedule time.
		x = sched_service(z)
		assert x.get_schedule_time() == '13:06:00'


	#@pytest.mark.skip
	#@pytest.mark.xfail
	def test_scheduler_service_get_schedule_time(self):
		z = sched_model(self.cases.case0)
		z.obj['scheduled_time']['date'] = '2019-09-20'
		z.obj['scheduled_time']['time'] = '12:20am'
		assert type(z.obj) is dict

		x = sched_service(z)
		assert x.get_schedule_time() == '00:20:00'


	#@pytest.mark.skip
	@pytest.mark.xfail
	def test_scheduler_service_set_schedule_time(self):
		z = sched_model(self.cases.case0)
		z.obj['scheduled_time']['date'] = '2019-09-08'
		z.obj['scheduled_time']['time'] = '12:35am'
		assert type(z.obj) is dict

		x = sched_service(z)
		x.set_schedule_time()
		#x.run_pending_scheduled_jobs()

	#Test that the right day/hour/minute are correct and cause the job to write timestamp into
	#a file.
	# To Test this: create model. Use a case. set the correct desired date. Set correct desired time.	# Create service. Set scheduled time. Run job. Monitor the file.
