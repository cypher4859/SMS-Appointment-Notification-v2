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
		base_example = '23:2:4'
		trans = schedule_transformer(base_example)
		transformed_time = trans.transform_time_to_schedule_job_format()


		assert  transformed_time == '23:02:04', 'Cant transform the time correctly. Try again'

	#@pytest.mark.xfail
	def test_sched_service_get_utc_schedule_time(self):
		z = sched_model(datetime(2019, 8, 25, 15, 41, 19, 821795, tzinfo=pytz.utc))
		with pytest.raises(AssertionError):
			assert type(z.obj) is dict, 'The schedule model does not contain a dict'	

		x = sched_service(z.obj)
		with pytest.raises(AttributeError):
			assert x.get_schedule_time() == '15:41:19', 'Has no __dict__ property, the schedule model is not of type dict'

		#alt_z = sched_model(datetime(2019, 8, 25, 2, 1, 9, 821795, tzinfo=pytz.utc))
		#alt_x = sched_service(alt_z.obj)
		#assert alt_x.get_schedule_time() == '02:01:09', 'Could not pad zeros at right places'

		#alt2_z = sched_model(datetime(2019, 8, 25, 2, 12, 9, 821795, tzinfo=pytz.utc))
		#alt2_x = sched_service(alt2_z.obj)
		#assert alt2_x.get_schedule_time() == '02:12:09', 'Could not pad zeros at right places'

		#alt3_z = sched_model(datetime(2019, 8, 25, 2, 1, 19, 821795, tzinfo=pytz.utc))
		#alt3_x = sched_service(alt3_z.obj)
		#assert alt3_x.get_schedule_time() == '02:01:19', 'Could not pad zeros at right places'

		#alt4_z = sched_model(datetime(2019, 8, 25, 22, 1, 9, 821795, tzinfo=pytz.utc))
		#alt4_x = sched_service(alt4_z.obj)
		#assert alt4_x.get_schedule_time() == '22:01:09', 'Could not pad zeros at right places'

	#@pytest.mark.xfail
	def test_sched_service_get_tzaware_time_from_transformed_time(self):
		z = sched_model(datetime(2019, 8, 25, 22, 1, 9, 821795, tzinfo=pytz.utc))
		with pytest.raises(AssertionError):
			assert type(z.obj) is dict, 'The schedule model does not contain a dict'

		x = sched_service(z.obj)
		assert x.get_tz_aware_schedule_time() == z.obj.astimezone(timezone('US/Eastern'))

	def test_updated_distributor_sched_service_get_utc_schedule_time(self):
		z = sched_model(self.cases.case0)
		assert type(z.obj) is dict

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
