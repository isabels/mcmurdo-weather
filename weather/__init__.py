import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, render_template

from .data import boulder_temp, mcmurdo_temp


def compare(boulder, mcmurdo):
    if boulder is None or mcmurdo is None:
        return "WE JUST DON'T KNOW..."
    if boulder < mcmurdo:
        return "YES!"
    else: 
        return "NO"

def morning():
    pass

def time_of_day(hour):
    if hour < 6 or hour >= 22:
        return "night"
    elif hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"
    
def format_temp(temp):
    if temp is None:
        return "N/A"
    else:
        return "{:.1f} °F".format(temp)

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def index():
        boulder = boulder_temp()
        mcmurdo = mcmurdo_temp()
        answer = compare(boulder, mcmurdo)
        btz = ZoneInfo("America/Denver")
        mtz = ZoneInfo("Antarctica/McMurdo")
        now = datetime.now(tz=btz)
        data = {"answer": answer, 
                "btime": now.strftime("%A, %B %d, %Y at %H:%M"), 
                "mtime": now.astimezone(tz=mtz).strftime("%H:%M"),
                "boulder": format_temp(boulder),
                 "mcmurdo": format_temp(mcmurdo),
                 "time_of_day": time_of_day(now.hour)}
        return render_template('index.html', data=data)

    return app
