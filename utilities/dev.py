#!/usr/bin/python3.7

import ipdb as pdb
import json
import os
from pymongo import MongoClient

def get_template():
	#Get the JSON template structure
	appointment = {
		'chart_number': '',
		'recipient': '',
		'name': '',
		'date_created': '',
		'appointment': {
			'date': '',
			'time': '',
			'status': '',
		},
		'doctor': '',
		'message': '',
		'care_provider': '',
		#token from vault
		'sender': '',
		'acct': '',
		'token': ''
	}

	return appointment


'''def get_values(key=None):
	possible_keys = ['chart_number', 'phone', 'name', 'date_created', 'appointment', 'doctor', 'message', 'care_provider', 'atotal_id']
	if(key != None):
		for x in possible_keys:
			if(key == x):
				#return the value
	return'''

def get_fields():
	possible_keys = ['chart_number', 'recipient', 'name', 'date_created', 'appointment', 'doctor', 'message', 'care_provider', 'sender', 'acct', 'token']
	return possible_keys

# sample data = dev.design_custom_template('0BX01111', '3044446329', 'fuckthisplace', '05/05/2019', '05/06/2019', '3:15 PM', 'Confirmed', 'Childers', 'fuckkk', 'childersandtaylor', 'auth_token_from_vault')
# sample data = dev.design_custom_template('0FX06666', '3044446329', 'getoutofher', '05/04/2019', '05/07/2019', '4:15 PM', 'Unconfirmed', 'Childers', 'fuckkk', 'childersandtaylor', 'auth_token_from_vault')
# sample data = dev.design_custom_template('0CX42069', '3044446329', 'ahhhh sly marbo', '06/05/2019', '06/06/2019', '1:15 PM', 'Unconfirmed', 'Childers', 'fuckkk', 'childersandtaylor', '3046664200', 'some_acct_SID', 'auth_token_from_vault')



def design_custom_template(chart=None, 
			recipient=None, 
			name=None,
			createDate=None,
			appDate=None,
			appTime=None,
			appStat=None,
			doc=None,
			msg=None,
			provider=None,
			sender=None,
			acct=None,
			token=None):

	temp = get_template()
	########################
	# minify the variables #
	########################
	c, rec, n, cd, appd, appt, apps, d, m, p, send, act, tok = chart, recipient, name, createDate, appDate, appTime, appStat, doc, msg, provider, sender, acct, token
	vals = [c, rec, n, cd, appd, appt, apps, d, m, p, send, tok]
	i = 0; ii = 0
	for key in temp:
		if(key == 'appointment'):
			for weird in temp[key]:
				temp[key][weird] = vals[i]
				i += 1
			continue
		else:
			temp[key] = vals[i]
			i += 1

	return temp

def insert_one_appointment(payload):
	# deserialized?
	# RUN THROUGH THE design_custom_template() first! Pump that into here
	try:
		client = MongoClient('mongodb://localhost:27017/')
		db = client.test_database
		db.inventory.insert_one(payload)
		print('successfully inserted the document')
	except:
		print('fucked up')

def insert_many_appointment(payload):	
	try:
		import ipdb; ipdb.set_trace()
		client = MongoClient('mongodb://localhost:27017/')
		db = client.test_database
		db.inventory.insert_many(payload)
		print('successfully inserted many appointments')
	except:
		print('fucked up')





def find_docs(key=None, val=None):
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

####FIXXXXXX
def confirm_appt_status(patient, doctor, status):
	try:
		client = MongoClient('mongodb://localhost:27017/')
		db = client.test_database
		#db.inventory.update_many({'phone':phone, 'atotal_id':aID, 'appointment':{'date':apptDate}}, 'appointment':{'status':'Confirmed'})
		#import ipdb; ipdb.set_trace()
		db.inventory.update_many({ "$and": [{"patient_number": patient}, {"doctor_number": doctor}, {"appointment.status": "Unconfirmed"}]},{"$set": {"appointment.status": status}})
		#print(result.modified_count)
	except:
		print('fucked up')

def update_message_delivery_status(message_sid, status, acct):
	try:
		client = MongoClient('mongodb://localhost:27017/')
		db = client.test_database
		#pdb.set_trace()
		db.inventory.update({ "$and": [{'message_sid': message_sid}, {'acct': acct}]}, {'$set': {'delivery_status': status}})	
	except:
		print('fuck this place')

def get_all_collections():
	try:
		client = MongoClient('mongodb://localhost:27017/')
		db = client.test_database
		return db.collection_names()
	except:
		print('fucked up')

def read_all_appointments():
	try:
		client = MongoClient('mongodb://localhost:27017/')
		db = client.test_database
		docs = db.inventory.find()
		z = []
		for x in docs:
			z.append(x)

		return z
	except:
		print('do nothing')
