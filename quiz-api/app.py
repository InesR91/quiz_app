from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'tout le monde'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

if __name__ == "__main__":
    app.run()
    
	