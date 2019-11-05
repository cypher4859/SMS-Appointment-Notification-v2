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


	# Set like this it will set the job to run literally one day from now.
	# Setting this to run every minute and checking with accuracy down to the minute would do well.
	# Also. I thought I set schedule to run continuously?? Ahh, I did. Its set in the if __name__ in the controller.
	# 
	# Should we check for whether the time is set for today?
	# Conclusion: If the scheduled date is for today then schedule it for every minute, else if for date in future
	# run the scheduler job every day until that particular point
	#
	# This still doesn't solve the conditional statement in the job. We need to check with less degree of accuracy
	# than millisecond. Needs to be at the minute mark. I think. Try the every().miunte.at method first (checking for
	# job scheduled for today) first, it might show that its okay.
	def set_schedule_time(self):
		# Thinking this should be done every second to make sure that the jobs run correctly
		schedule.every().minute.do(self.job).tag('test-tasks', 'mine')


	def get_schedule_time(self):
		#Needs converted to datetime
		date_transform = generic_date(self.datetime.__dict__['obj']['scheduled_time'])
		dt_obj = date_transform.transform_into_datetime_object()	# This should convert the desired time into the UTC version

		orig_time = f'{dt_obj.hour}:{dt_obj.minute}:{dt_obj.second}'

		transformer = schedule_transformer(orig_time)
		return transformer.transform_time_to_schedule_job_format()

	# The datetime attribute needs to be a datetime function for this to work.
	# There should be a check to ensure that datetime is what gets inputted.
	def get_schedule_date(self):
		#Needs converted to datetime
		date_transform = generic_date(self.datetime.__dict__['obj']['scheduled_time'])
		dt_obj = date_transform.transform_into_datetime_object()

		orig_time = f'{dt_obj.year}-{dt_obj.month}-{dt_obj.day}'
		return orig_time



	def job(self):
		# Process current and desired day
		desired_day = self.get_schedule_date() # Return in Y-m-d in UTC
		current_day = datetime.utcnow().strftime('%Y-%m-%d') # in UTC


		# Process current and desired time
		t = self.get_schedule_time() # return time in HH:MM:SS
		desired_hour_and_minute = t.split(':')[0] + ':' + t.split(':')[1] # Filter to HH:MM
		current_hour_and_current_min = datetime.utcnow().strftime('%H:%M') # return in HH:MM

		with open('schedule_log_file', 'a+') as log:
			log.write(f"t's time: {t}")
			log.write(f"Current day = {current_day}   -   current time = {current_hour_and_current_min}\nDesired day = {desired_day}   -   Desired time = {desired_hour_and_minute}\n")

		if(current_day == desired_day and current_hour_and_current_min == desired_hour_and_minute):
			print('Call up the sms sender...')
			with open('test_file', 'w+') as f:
				f.write(f"Current datetime is: {datetime.now()}")
			return schedule.CancelJob
		

	def get_tz_aware_schedule_time(self):
		# This requests the transformer to convert the utc date object into a tz aware date object
		transformer = timezone_transformer(self.datetime, 'US/Eastern')
		return transformer.transform_utc_to_timezone_object()

	def clear_schedule_time(self):
		schedule.clear('test-tasks')
