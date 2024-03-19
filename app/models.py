from app import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(244))
    description = db.Column(db.String(255))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(25))
    location = db.Column(db.String(244))
    
    def __init__(self, title, description, rooms, bathrooms, price, property_type, location):
        self.title= title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
   
    
    def __repr__(self):
        return '<Property %r>' % self.title
