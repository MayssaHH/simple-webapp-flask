import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/health')
def health():
    return jsonify(status='OK'), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
