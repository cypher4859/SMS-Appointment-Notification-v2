import schedule
import time
from datetime import datetime
from sms_v2.models.schedule_model import sched_model
from sms_v2.transformers.sched_transformer import schedule_transformer
from sms_v2.transformers.timezone_transformer import timezone_transformer

class sched_service:
	def __init__(self, datetime_model):
		self.datetime = datetime_model


	def job(self):
		if(datetime.utcnow().date() == self.get_date()):
			print('Do things...')
			return schedule.CancelJob

	def set_time(self):
		#import ipdb; ipdb.set_trace()
		schedule.every().day.at(self.get_schedule_time()).do(self.job)

	def get_schedule_time(self):
		orig_time = f'{self.datetime.hour}:{self.datetime.minute}:{self.datetime.second}'
		transformer = schedule_transformer(orig_time)
		return transformer.transform_time_to_schedule_job_format()

	def get_date(self):
		return self.datetime.date()


	def get_tz_aware_schedule_time(self):
		# This requests the transformer to convert the utc date object into a tz aware date object
		transformer = timezone_transformer(self.datetime, 'US/Eastern')
		return transformer.transform_utc_to_timezone_object()
