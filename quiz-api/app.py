from flask import Flask, request, jsonify
from flask_cors import CORS
from jwt_utils import build_token, decode_token, JwtError

app = Flask(__name__)
CORS(app)

PASSWORD = "test"


@app.route('/')
def hello_world():
	x = 'tout le monde'
	return f"Hello, {x}"


@app.route('/login', methods=['POST'])
def login():
	payload = request.get_json(force =True)
	password = payload.get("password", None)
	if password != PASSWORD:
		return {"message": "Wrong Password "}, 401

	token = build_token()
	return {"token": token}, 200 
	

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

if __name__ == "__main__":
    app.run()
    
	