from app import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(244))
    description = db.Column(db.String(255))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.String(120))
    property_type = db.Column(db.String(25))
    location = db.Column(db.String(244))
    filename = db.Column(db.String(255))
    
    def __init__(self, title, description, rooms, bathrooms, price, property_type, location, filename):
        self.title= title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.filename = filename
   
    
    def __repr__(self):
        return '<Property %r>' % self.title
