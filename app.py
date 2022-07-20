import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello</h1>'


if __name__ == '__main__':
    debug = eval(os.environ.get('DEBUG', 'False'))
    app.run(debug=debug)