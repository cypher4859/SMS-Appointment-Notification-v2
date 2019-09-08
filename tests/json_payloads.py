
class json_payloads:
	headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json'
	}

	test_receive_sms_reply_json_payload = {
		"account_sid": "AC471e900502c9d036fa8cc7e6a50682e9",
		"api_version": "2010-04-01",
		"body": "Y",
		"date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
		"date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
		"date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
		"direction": "outbound-api",
		"error_code": None,
		"error_message": None,
		"from": "+13044446329",
		"messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
		"num_media": "0",
		"num_segments": "1",
		"price": "-0.00750",
		"price_unit": "USD",
		"sid": "MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
		"status": "sent",
		"subresource_uris": {
			"media": "/2010-04-01/Accounts/AC471e900502c9d036fa8cc7e6a50682e9/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
		},
		"to": "+13047605956",
		"uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
	}

	test_notify_json_payload = [{
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": ""
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"timezone": "US/Eastern"
		}
	}]

	test_negative_sms_sender_json_payload = {
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": ""
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"timezone": "US/Eastern"
		}
	}

	test_receive_sms_status_json_payload = {
		"SmsSid": "SMabd7164713414a9e821beb4456c98b82",
		"SmsStatus": "delivered",
		"MessageStatus": "delivered",
		"To": "+13044446329",
		"MessageSid": "SMabd7164713414a9e821beb4456c98b82",
		"AccountSid": "AC471e900502c9d036fa8cc7e6a50682e9",
		"From": "+13047605956",
		"ApiVersion": "2010-04-01"
	}




class test_schedule_cases_jsons:
	case0 = {
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": "US/Eastern"
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"timezone": "US/Eastern"
		}
	}

	case1 = {
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": "US/Eastern"
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-25",
			"time": "11:06pm",
			"timezone": "US/Eastern"
		}
	}

	case2 = {
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": "US/Eastern"
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"timezone": "US/Eastern"
		}
	}

	case3 = {
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": "US/Eastern"
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"timezone": "US/Eastern"
		}
	}

	case4 = {
		"chart": "someChart",
		"patient_number": "3044446329",
		"name": "testting",
		"date_created": "",
		"appointment": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"status": "Unconfirmed",
			"timezone": "US/Eastern"
		},
		"doctor": "Dr. Strange",
		"message": "Test new system",
		"doctor_office": "The Office",
		"doctor_number": "3047605956",
		"acct": "AC471e900502c9d036fa8cc7e6a50682e9",
		"token": "",
		"secret_name": "childerstaylor",
		"delivery_status": "",
		"scheduled_time": {
			"date": "2019-08-20",
			"time": "1:06pm",
			"timezone": "US/Eastern"
		}
	}

