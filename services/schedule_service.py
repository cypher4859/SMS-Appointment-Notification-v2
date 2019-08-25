import schedule
import time
from datetime import datetime
from sms_v2.models.schedule_model import sched_model

class sched_service:
	def job(self, date):
		if(datetime.utcnow().date() == date):
			print('Do things...')
			return schedule.CancelJob

	def set_time(self, t, date):
		#import ipdb; ipdb.set_trace()
		schedule.every().day.at(t).do(self.job, date)



def main():
	sched_mod = sched_model(datetime.utcnow())
	sched_serv = sched_service()

	sched_serv.set_time('23:10:02', sched_mod.get_date())
