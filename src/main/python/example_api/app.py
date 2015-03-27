__author__ = 'mhoyer'

from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"


app.run('0.0.0.0', '8080', threaded=True)