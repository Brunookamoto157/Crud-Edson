from flask import render_template
from app import app
from app.controllers import api

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')