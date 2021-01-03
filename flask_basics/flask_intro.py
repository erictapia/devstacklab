from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# How to run flask in dev environment
#   export FLASK_APP=flask_intro.py
#   python -m flask run
#
#   Visit: http://127.0.0.1:5000