from datetime import datetime

class date:
	def __init__(self, original_date):
		self.date = original_date['date']
		self.time = original_date['time']
		self.status = original_date['status']

	def transform_get_full_date(self):
		date = datetime.strptime(self.date, '%Y-%m-%d')
		time = datetime.strptime(self.time, '%I:%M%p')
		final_date = datetime(date.year, date.month, date.day, time.hour, time.minute)

		utc_date_object = { 'date': date, 'time': time, 'status': self.status, 'fulldate': final_date}

		return utc_date_object
