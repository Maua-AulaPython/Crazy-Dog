from server import db



class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    measures=db.relationship('Measure')
        


    
class Measure(db.Model):
    id_device = db.Column(db.Integer, db.ForeignKey('device.id'))
    luminosity = db.Column(db.Float)
    temperature = db.Column(db.Float)
    date = db.Column(db.DateTime, primary_key=True)
