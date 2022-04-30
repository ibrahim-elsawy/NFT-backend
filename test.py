from google.oauth2 import id_token
from google.auth.transport import requests
# from jose import jwt
import jwt

# (Receive token by HTTPS POST)
# ...
CLIENT_ID = "607168265706-k6pvnqm47a7v168h2k7kkg3frn4qi3s5.apps.googleusercontent.com"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJZCI6Ijg1ZDcyNGRiLWJkOWMtNDg2OC04ZTkwLWQwNzVmNDQzZGVmNCIsImVtYWlsIjoiYW1yZWxzYXd5QGdtYWlsLmNvbSIsInN1YiI6ImFtcmVsc2F3eUBnbWFpbC5jb20iLCJqdGkiOiI5ZDRiYzc3MS03YTBhLTRkYzEtOGI0MC04NzBkZGExNDdhYjYiLCJuYmYiOjE2Mjg3MzUxMzAsImV4cCI6MTYyODczNTE2MCwiaWF0IjoxNjI4NzM1MTMwfQ.0tC8N77Sdkad22B3pKim4w7A71hkEQG_qVTa_Idt1aE"
# dec = jwt.decode(token, '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', algorithms=['HS256'])
idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID) 
userid = idinfo['sub']
