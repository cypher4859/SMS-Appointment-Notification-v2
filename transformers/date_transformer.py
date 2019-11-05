from datetime import datetime

class date:
	def __init__(self, original_date):
		self.date = original_date['date']
		self.time = original_date['time']
		self.timezone = original_date['timezone']
		if(original_date['status']):
			self.status = original_date['status']


	def transform_get_full_date(self):
		date = datetime.strptime(self.date, '%Y-%m-%d')
		time = datetime.strptime(self.time, '%I:%M%p')
		final_date = datetime(date.year, date.month, date.day, time.hour, time.minute)

		utc_date_object = { 'date': date, 'time': time, 'status': self.status, 'fulldate': final_date, 'timezone': self.timezone}
		#import ipdb; ipdb.set_trace()
		return utc_date_object

	def transform_into_datetime_object(self):
		date = datetime.strptime(self.date, '%Y-%m-%d')
		time = datetime.strptime(self.time, '%I:%M%p')
		return datetime(date.year, date.month, date.day, time.hour, time.minute, tzinfo=pytz.utc)
