import datetime
from flask import Flask
from markupsafe import escape


app = Flask(__name__)

# Converter type: string - (default) accepts any text without a slash
@app.route('/hello/<string:username>')
def hello_username(username):
    return f'Hello { escape(username) }!'

# Converter type: int - accepts positive integers
@app.route('/echo/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

# Converter type: int - accepts positive integers
@app.route('/float/<float:fraction>')
def show_float(fraction):
    return f'Fraction: {fraction}'

# Converter type: path - like string but also accepts slashes
@app.route('/api/v0/<path:subpath>')
def api_v0(subpath):
    return f'The subpath is: { escape(subpath) }'

# Converter type: uuid - accepts UUID strings (32 hex)
@app.route('/uuid/<uuid:uuid>')
def show_uuid(uuid):
    return f'UUID: {uuid}'

@app.route('/')
def index():
    return f'{datetime.datetime.now()}'


# How to run flask in dev environment
#   export FLASK_APP=flask_intro.py
#   python -m flask run
#
#   Visit: http://127.0.0.1:5000