from threading import Event
from app import app
from flask import render_template, request
from models.event_list import events
from models.event import Event

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/new-event')
def add_event():
    return render_template('new-event.html')

@app.route('/new-event', methods=['POST'])
def new_event():
    form = request.form
    print(type(form['event-date']))
    new_event = Event(form['event-date'], form['event-name'], int(form['guests']), form['location'], form['description'])
    events.append(new_event)
    return render_template('index.html', events=events)