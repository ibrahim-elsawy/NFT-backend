from cgitb import handler
from flask import Flask, make_response, request, jsonify, send_file, Response
import os
from waitress import serve
from PIL import Image
import sys
from flask_cors import CORS
from middleware import HandleRequest
sys.path.append("pixray")

import os
os.environ['ENV'] = 'production'

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
PORT = os.environ.get("PORT")

@app.route("/nft", methods=["POST"])
def nft():
	if request.method == "POST":
		try:
			#TODO
			#[x] naming of the output image from the model

			req = {}
			req["x-auth"] = request.headers['x-auth']
			req["prompt"] = request.form["prompt"]
			req["keyword"] = request.form["keyword"]
			req["quality"] = request.form["quality"]
			req["type"] = request.form["type"]
			req["aspect"] = request.form["aspect"]
			req['initImage'] = None if len(request.files)==0 else Image.open(request.files['initImage'])
			req["publish"] = False if request.form["publish"] == "false" else True
			handler = HandleRequest()
			# res = handler.createNft(req)
			res = {}
			if res == False:
				return make_response(jsonify({"msg": "unvalid token"}), 400)
			return send_file(res)
		except KeyError:
			return Response(status=400)


@app.route("/num", methods=['GET'])
def get_numImages(): 
	if request.method == 'GET': 
		try: 
			handler = HandleRequest()
			return jsonify({"num":handler.getNumImages()})
		except Exception as e: 
			return Response(status=400)


@app.route("/images", methods=['POST'])
def get_images(): 
	if request.method == 'POST': 
		try: 
			req = request.get_json() 
			handler = HandleRequest()
			return jsonify(handler.getImages(req))

		except Exception as e: 
			return Response(status=400)



@app.route("/interact", methods=['POST'])
def interact(): 
	if request.method == 'POST': 
		try: 
			req = request.get_json() 
			req['x-auth'] = request.headers['x-auth']
			handler = HandleRequest()
			handler.actionLike(req)
			return Response(status=200)
		except Exception as e: 
			return Response(status=400)

@app.route("/checklike", methods=['POST'])
def checkLike(): 
	if request.method == 'POST': 
		try: 
			req = request.get_json() 
			req['x-auth'] = request.headers['x-auth']
			handler = HandleRequest()
			res = handler.checkLike(req)
			return jsonify(res) 
		except Exception as e: 
			return Response(status=400)


			
if __name__ == '__main__':

	port = int(os.environ.get('PORT', 5000)) 
	# app.run(app, port=port)
	serve(app, host="0.0.0.0", port=PORT) 
