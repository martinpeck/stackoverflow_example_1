import os
from flask import Flask


basedir = os.path.abspath(os.path.dirname(__file__))

from landingpage import app

# app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)