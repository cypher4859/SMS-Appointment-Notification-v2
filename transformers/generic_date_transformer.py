from datetime import datetime

import pytz

class generic_date:
	def __init__(self, d):
		self.date = d['date']
		self.time = d['time']
		self.timezone = d['timezone']

	def transform_into_datetime_object(self):
		date = datetime.strptime(self.date, '%Y-%m-%d')
		time = datetime.strptime(self.time, '%I:%M%p')
		return datetime(date.year, date.month, date.day, time.hour, time.minute, tzinfo=pytz.utc)
