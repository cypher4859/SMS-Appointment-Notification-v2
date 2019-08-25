
class sched_model:
	def __init__(self, date):
		self.obj = date

	def get_time(self):
		return f'{self.obj.hour}:{self.obj.minute}:{self.obj.second}'

	def get_date(self):
		return self.obj.date()

	def get_full_date(self):
		return self.obj
