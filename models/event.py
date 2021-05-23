class Event:
    def __init__(self, date, name, no_of_guests, location, description):
        self.date = date
        self.name = name
        self.no_of_guests = no_of_guests
        self.location = location
        self.description = description
        self.id = id(self)
    
    def __string__(self):
        return str(vars(self))
        