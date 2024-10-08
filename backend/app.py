from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask B555555555ackend1!"
    return "Welcome to the Flask B55555ackend!"

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Flask!")

@app.route('/test')
def test():
    return "Test route works!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)