from flask import Flask, request, jsonify
from flask_cors import CORS
from jwt_utils import build_token, decode_token, JwtError
import sqlite3
import os
from models import Question

app = Flask(__name__)
CORS(app)

PASSWORD = "test"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "quiz_bdd_prime.db")


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

@app.route('/questions', methods=['POST'])
def add_question():
    
	# Récupérer le token (même si on ne le valide pas encore)
    token = request.headers.get('Authorization')
    print("Token reçu :", token)  # Debug

    # Récupérer le JSON du body
    data = request.get_json()
    print("Données reçues :", data)  # Debug


    # Créer un objet Question
    question = Question(
        position=data.get("position"),
        title=data.get("title"),
        text=data.get("text"),
        image=data.get("image")
    )

    # Sauvegarde en BDD
    question.save(DB_PATH)

    return {"message": "Question ajoutée avec succès"}, 201

if __name__ == "__main__":
    app.run()
    
	