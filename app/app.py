from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/a')
def route_a():
    return 'route_a'


@app.route('/b')
def route_b():
    return 'route_b'
