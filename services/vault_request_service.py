import requests

class vault_request:
	def __init__(self, secret_name):
		self.secret_name = secret_name
		self.vault_url = "http://localhost:8200/v1/atotalwv_customers/"
		self.vault_token = "s.uIvnkUEqR5jLikwEtHWTlmhP"
		self.head = {'X-Vault-Token':self.vault_token}	
		self.url = f"{self.vault_url}{self.secret_name}"
		
	def request_token(self):
		res = requests.get(self.url, headers=self.head)
		return res.json()['data']['authtoken']

	def request_sid(self):
		res = requests.get(self.url, headers=self.head)
		return res.json()['data']['sid']
