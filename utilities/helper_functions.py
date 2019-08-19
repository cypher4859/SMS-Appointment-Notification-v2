import json
import os
import datetime
from bson.son import SON
from pymongo import MongoClient

class dev:
	def get_template(self):
		print('')

	def get_fields(self):
		print('')

	def design_custom_template(self):
		print('')

	def insert_one_appointment(self, payload):
		try:
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			db.inventory.insert_one(payload)
			print('successfully inserted the document')
		except:
			print('fucked up')

	def insert_many_appointment(self, payload):
		try:
			import ipdb; ipdb.set_trace()
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			db.inventory.insert_many(payload)
			print('successfully inserted many appointments')
		except:
			print('fucked up')


	def find_docs(self, key=None, val=None):
		try:
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			if(key != None and val != None):
				doc = db.inventory.find({key:val})
				return doc
				for x in doc:
					print(x)
			else:
				doc = db.inventory.find({})
				return doc
				for x in doc:
					print(x)
		except:
			print('fucked up')

	def confirm_appt_status(self, patient, doctor, status, acct):
		try:
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			pipeline = [{ '$match': { '$and': [
                            {'patient_number': patient},
                            {'doctor_number': doctor},
                            {'appointment.status': "Unconfirmed"},
                            {'acct': acct}
                            ]}
                        },
                        {
                            '$project' : {
                                'patient_number': 1,
                                'doctor_number': 1,
                                "appointment.status": 1,
                                "appointment.date": 1,
                                "appointment.fulldate" : 1,
                                'message_sid': 1,
                                'difference' : {
                                    '$abs' : {
                                        '$subtract' : [datetime.datetime.utcnow(), "$appointment.fulldate"]
                                    }
                                }
                            }
                        },
                        {
                            '$sort' : SON({'difference' : 1})
                        },
                        {
                            '$limit' : 1
                        }
                	]
			document_to_update = list(db.inventory.aggregate(pipeline))[0]
			db.inventory.update({'message_sid': document_to_update['message_sid']}, {'$set': {'appointment.status': status}})
		except:
			print('')

	def update_message_delivery_status(self, message_sid, status, acct):
		try:
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			db.inventory.update({ "$and": [{'message_sid': message_sid}, {'acct': acct}]}, {'$set': {'delivery_status': status}})
		except:
			print('')

	def get_all_collections(self):
		try:
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			return db.collection_names()
		except:
			print('fucked up')



	def read_all_appointments(self):
		try:
			client = MongoClient('mongodb://localhost:27017/')
			db = client.test_database
			docs = db.inventory.find()
			z = []
			for x in docs:
				z.append(x)

			return z
		except:
			print('')

