import schedule
import time
from datetime import datetime
from sms_v2.models.schedule_model import sched_model
from sms_v2.transformers.sched_transformer import schedule_transformer

class sched_service:
	def __init__(self, t_model):
		self.time = t_model


	def job(self):
		if(datetime.utcnow().date() == self.get_date()):
			print('Do things...')
			return schedule.CancelJob

	def set_time(self):
		#import ipdb; ipdb.set_trace()
		schedule.every().day.at(self.get_schedule_time()).do(self.job)

	def get_schedule_time(self):
		orig_time = f'{self.time.hour}:{self.time.minute}:{self.time.second}'
		trans = schedule_transformer(orig_time)
		return trans.transform_time()

	def get_date(self):
		return self.time.date()

