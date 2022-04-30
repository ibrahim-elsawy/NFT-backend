from createNft import createNft
from utils.Database import Database
from utils.Date import calculateDate 
from utils.Encryption import Encryption
import datetime
import base64


class HandleRequest():
	def __init__(self) -> None:
		self.data = Database("NFT.db")
		self.token = Encryption()
	# 	pass

	def createNft(self, req):

		try:
			user_info = self.token.decode(req["x-auth"])
		except Exception as e:
			return False
		row = self.data.getRowsWithFilter("users", "id", str(user_info['sub']))

		if len(row) != 0: 
			self.data.insert('users', values=[user_info['sub'], user_info['email'], user_info['name']])
		imageDir = str(user_info["id"]+".png")
		createNft(req["prompts"], req["quality"], req["aspect"], req["keyword"], req.get("initImage"), req["type"], imageDir)
		if req["publish"] == True:
			now = datetime.datetime.today() 
			self.data.insert("images", [user_info["id"], str(user_info["id"]+".png"), 0, now.year, now.month, now.day, now.hour, now.minute, req["prompts"]])
		return imageDir

	
	def getNumImages(self):
		return self.data.getNumRows("images")

	def getImages(self, req):
		
		images64 = []
		ids = []
		likes = []
		dates = []
		users = []
		title = []
		offset = req['offset']
		limit = req['limit']
		rows = self.data.getRowsWithFilterLimit("images", limit=limit, offset=offset)
		for r in rows:
			fileDir = r[2] 
			image = open(fileDir, 'rb') 
			image_read = image.read()
			byteImage = base64.b64encode(image_read)
			# images64.append(str(byteImage).replace("'","").replace("b", ""))
			images64.append("data:image/png;base64,"+byteImage.decode("ascii"))
			ids.append(str(r[0]))
			likes.append(r[3])
			dates.append(calculateDate(r[4], r[5], r[6], r[7], r[8])) #[4, "months"]
			users.append(self.data.getRowsWithFilter("users", "id", r[1])[0][3])
			title.append(r[-1])
			
		return {"ids":ids, "images":images64, "likes":likes, "date": dates, "user":users, "title":title}
		

	def actionLike(self, req):
		try:
			user_info = self.token.decode(req["x-auth"])
		except Exception as e:
			return False
		image_id = int(req["image_id"])
		# row = self.data.getRowsWithFilter("likes", "user_id", str(user_info['sub']))
		row = self.data.getRowsWithFilter("likes", "image_id", image_id)
		numLike = self.data.getRowsWithFilter("images", "i", image_id)[0][3]
		for r in row:
			if r[1] == str(user_info["sub"]):
				#dislike
				self.data.updateRowsWithFilter("images", "like", numLike-1, "i", image_id)
				self.data.deleteRowsWithFilter("likes", ["user_id", "image_id"], [str(user_info["sub"]), image_id])
				return True

		
		#like
		self.data.updateRowsWithFilter("images", "like", numLike+1, "i", image_id)
		self.data.insert("likes", [str(user_info["sub"]), int(image_id), 1])
	
	def checkLike(self, req):
		try:
			user_info = self.token.decode(req["x-auth"])
		except Exception as e:
			return False
		image_id = int(req["image_id"])
		# row = self.data.getRowsWithFilter("likes", "user_id", str(user_info['sub']))
		row = self.data.getRowsWithFilter("likes", "image_id", image_id)
		numLike = self.data.getRowsWithFilter("images", "i", image_id)[0][3]
		for r in row:
			if r[1] == str(user_info["sub"]):
				#already like this post
				return {"action":1}

		
		#doesn't like this post
		return {"action":0}