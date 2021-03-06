
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""echo "Running Flask App"
flask run
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

