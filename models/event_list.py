from models.event import Event
import datetime

event_1 = Event(datetime.date(2021, 5, 17), "Barbecue", 100, "Steve's House", "Let's all ome round for a barbecue", True)
events = [event_1]

def remove_event_with_id(id):
    id = int(id)
    for event in events:
        if event.id == id:
            events.remove(event)
            break
