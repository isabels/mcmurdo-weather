import os
from datetime import datetime

from flask import Flask, render_template

from .data import boulder_temp, mcmurdo_temp


def compare(boulder, mcmurdo):
    if boulder < mcmurdo:
        return "YES!"
    else: 
        return "NO"

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def index():
        boulder = boulder_temp()
        mcmurdo = mcmurdo_temp()
        answer = compare(boulder, mcmurdo)
        data = {"answer": answer, 
                "time": datetime.now().strftime("%A, %B %d, %Y at %H:%M:%S MDT"), 
                "boulder": boulder,
                 "mcmurdo": mcmurdo}
        return render_template('index.html', data=data)

    return app
