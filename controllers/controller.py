from app import app
from flask import render_template
from models.event_list import events

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/new-event')
def add_event():
    return render_template('new-event.html')