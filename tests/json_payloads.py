
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

	test_receive_sms_status_json_payload = {
		"Timestamp": "2019-08-13T01:10:56.458401Z",
		"Method": "POST",
		"RemoteAddr": "54.224.52.11",
		"ID": 368790053,
		"Headers": {
			"Accept": [
				"*/*"
			],
			"Cache-Control": [
				"max-age=259200"
			],
			"Content-Length": [
				"237"
			],
			"Content-Type": [
				"application/x-www-form-urlencoded; charset=utf-8"
			],
			"Host": [
				"ptsv2.com"
			],
			"User-Agent": [
				"TwilioProxy/1.1"
			],
			"X-Cloud-Trace-Context": [
				"652f20f755632e340ea127b0a8c6a1fd/3316521581287268365"
			],
			"X-Google-Apps-Metadata": [
				"domain=gmail.com,host=ptsv2.com"
			],
			"X-Twilio-Signature": [
				"gC6e/93+SYiWNWcQpLTpXPsOMwc="
			]
		},
		"FormValues": {
			"AccountSid": [
				"AC471e900502c9d036fa8cc7e6a50682e9"
			],
			"ApiVersion": [
				"2010-04-01"
			],
			"From": [
				"+13047605956"
			],
			"MessageSid": [
				"SMe477edca2300404a96a1bead62ee0c87"
			],
			"MessageStatus": [
				"delivered"
			],
			"SmsSid": [
				"SMe477edca2300404a96a1bead62ee0c87"
			],
			"SmsStatus": [
				"delivered"
			],
			"To": [
				"+13044446329"
			]
		},
		"Body": "",
		"Files": None,
		"MultipartValues": None
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

