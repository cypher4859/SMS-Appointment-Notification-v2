from pytz import timezone

class timezone_transformer:
	def __init__(self, dateobj, tz):
		self.date = dateobj
		self.tz = tz
		assert self.tz == 'US/Eastern', 'The timezone is wrong!'

	def transform_utc_to_timezone_object(self):
		return self.date.astimezone(timezone(self.tz))
