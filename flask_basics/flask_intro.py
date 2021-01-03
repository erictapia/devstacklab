import datetime
from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/hello/<username>')
def hello_username(username):
    return f'Hello { escape(username) }!'

@app.route('/echo/<int:post_id>')
def show_post(post_id: int):
    return f'Post {post_id}'

@app.route('/api/v0/<path:subpath>')
def api_v0(subpath):
    return f'The subpath is: { escape(subpath) }'

@app.route('/')
def index():
    return f'{datetime.datetime.now()}'


# How to run flask in dev environment
#   export FLASK_APP=flask_intro.py
#   python -m flask run
#
#   Visit: http://127.0.0.1:5000