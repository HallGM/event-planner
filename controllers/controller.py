from threading import Event
from app import app
from flask import render_template, request
from models.event_list import events, remove_event_with_id
from models.event import Event
import datetime

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/new-event')
def add_event():
    return render_template('new-event.html')

@app.route('/new-event', methods=['POST'])
def new_event():
    form = request.form
    recurring = bool(form.get('recurring'))
    new_date = datetime.date.fromisoformat(form['event-date'])   
    new_event = Event(new_date, form['event-name'], int(form['guests']), form['location'], form['description'], recurring)
    events.append(new_event)
    return render_template('index.html', events=events)

@app.route('/delete/<id>', methods=['POST'])
def delete_event(id):
    remove_event_with_id(id)
    return render_template('index.html', events=events)