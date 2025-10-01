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

@app.route('/questions', methods=['GET'])
def get_question_by_position():
    # Récupérer le paramètre "position" de l'URL
    position = request.args.get("position", type=int)

    if position is None:
        return jsonify({"error": "Le paramètre 'position' est requis"}), 400

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Pour obtenir un dict
        cur = conn.cursor()

        # Requête SQL pour récupérer la question par position
        cur.execute("SELECT * FROM Question WHERE position = ?", (position,))
        row = cur.fetchone()
        conn.close()

        if row is None:
            return jsonify({"message": "Aucune question à cette position"}), 404

        question = dict(row)
        return jsonify(question), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/questions/<int:questionId>', methods=['GET'])
def get_question_by_id(questionId):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM Question WHERE id = ?", (questionId,))
        row = cur.fetchone()
        conn.close()

        if row is None:
            return jsonify({"message": "Question introuvable"}), 404

        question = dict(row)
        return jsonify(question), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == "__main__":
    app.run()
    
	