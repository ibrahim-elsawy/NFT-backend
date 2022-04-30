from google.oauth2 import id_token
from google.auth.transport import requests

class Encryption():
	
	def __init__(self) -> None:
		self.request = requests.Request()


	def decode(self, token):
		decodeInfo = id_token.verify_oauth2_token(token, self.request, "607168265706-k6pvnqm47a7v168h2k7kkg3frn4qi3s5.apps.googleusercontent.com")
		return decodeInfo	