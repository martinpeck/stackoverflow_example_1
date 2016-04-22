import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask import Flask, render_template, session, redirect, url_for, current_app


import landingpage
from landingpage import app


@app.route('/', methods=['GET', 'POST'])
def index():

    return "hello"