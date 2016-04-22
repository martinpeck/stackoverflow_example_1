import os

from flask import Flask, render_template, session, redirect, url_for


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

import landingpage.views

