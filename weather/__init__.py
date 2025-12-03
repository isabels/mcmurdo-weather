import os
from datetime import datetime

from flask import Flask, render_template


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def index():
        data = {"answer": "YES!", "time": datetime.now().strftime("%A, %B %d %Y at %H:%M:%S"), "boulder": 30, "mcmurdo": 35}
        return render_template('index.html', data=data)

    return app
