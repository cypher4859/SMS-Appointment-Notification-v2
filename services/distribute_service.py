from sms_v2.services.sms_send_service import sms
from sms_v2.services.schedule_service import sched_service
from sms_v2.models.schedule_model import sched_model

class distributor:
	def __init__(self, collection):
		self.collection = collection

	def distribute_to_sender(self):
		for index, message in enumerate(self.collection):
			sender_service = sms(message)
			sender_service.load()
			

	def distribute_to_scheduler(self):
		for index, message in enumerate(self.collection):
			# Does this need to go to the schedule transformer first,
			# because it needs a datetime object in the date and the time
			# rather than a string in order to do schedule things on it.

			# It should never have to transform it back into a string, to my knowledge
			a = sched_model(message)
			b = sched_service(a)
			b.set_schedule_time()
