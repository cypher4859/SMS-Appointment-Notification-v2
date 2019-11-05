class schedule_transformer:
	def __init__(self, t):
		self.time = t
		assert type(self.time) is str
		assert len(self.time) < 9 and len(self.time) > 4


	def transform_time_to_schedule_job_format(self):
		fixed_time = ''
		for index, unit in enumerate(self.time.split(':')):
			if(len(unit) < 2):
				fixed_time += f'0{unit}'
			elif(len(unit) == 2):
				fixed_time += unit
			else:
				pass

			if(index != 2):
				fixed_time += ':'

		return fixed_time
