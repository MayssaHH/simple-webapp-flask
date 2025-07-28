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

@app.route('/error')
def trigger_error():
    raise RuntimeError('Intentional error')


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(error='Internal Server Error'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
