from google.oauth2 import id_token
from google.auth.transport import requests
import os

CLIENT_ID = os.environ.get("client_id")
class Encryption():
	
	def __init__(self) -> None:
		self.request = requests.Request()


	def decode(self, token):
		decodeInfo = id_token.verify_oauth2_token(token, self.request, str(CLIENT_ID))
		return decodeInfo	