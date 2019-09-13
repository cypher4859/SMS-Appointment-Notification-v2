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
			a = sched_model(message)
			b = sched_service(a)
			b.set_schedule_time()
