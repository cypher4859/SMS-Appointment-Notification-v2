import schedule
import time
from datetime import datetime
from sms_v2.models.schedule_model import sched_model
from sms_v2.transformers.sched_transformer import schedule_transformer
from sms_v2.transformers.timezone_transformer import timezone_transformer
from sms_v2.transformers.generic_date_transformer import generic_date

class sched_service:
	def __init__(self, datetime_model):
		self.datetime = datetime_model


	def set_schedule_time(self):
		#import ipdb; ipdb.set_trace()
		schedule.every().day.at(self.get_schedule_time()).do(self.job)


	def get_schedule_time(self):
		#Needs converted to datetime
		date_transform = generic_date(self.datetime.__dict__['obj']['scheduled_time'])
		dt_obj = date_transform.transform_into_datetime_object()

		orig_time = f'{dt_obj.hour}:{dt_obj.minute}:{dt_obj.second}'

		transformer = schedule_transformer(orig_time)
		return transformer.transform_time_to_schedule_job_format()


	def job(self):
		if(datetime.utcnow().date() == self.get_date()):
			print('Call up the sms sender...')
			return schedule.CancelJob
	

	def get_date(self):
		return self.datetime.date()


	def get_tz_aware_schedule_time(self):
		# This requests the transformer to convert the utc date object into a tz aware date object
		transformer = timezone_transformer(self.datetime, 'US/Eastern')
		return transformer.transform_utc_to_timezone_object()
