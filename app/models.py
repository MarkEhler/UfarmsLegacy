from app import db

class Ufarms(db.Model):
    __tablename__ = 'Ufarms'  # Set the custom table name
    UfarmID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer)
    Name = db.Column(db.String(255), unique=True)
    Host = db.Column(db.Boolean)
    IsActive = db.Column(db.Boolean)
    AddressStr = db.Column(db.String(255), unique=True)
    Contact = db.Column(db.String(255), unique=True)
    Request = db.Column(db.String(255))
    Privacy_lat = db.Column(db.Float)
    Privacy_lon = db.Column(db.Float)

    def serialize(self):
        return {
            'UfarmID': self.UfarmID,
            'UserID': self.UserID,
            'Name': self.Name,
            'Host': self.Host,
            'IsActive': self.IsActive,
            'AddressStr': self.AddressStr,
            'Contact': self.Contact,
            'Request': self.Request,
            'Privacy_lat': self.Privacy_lat,
            'Privacy_lon': self.Privacy_lon
        }
    
    def __repr__(self):
        return '<Ufarms {}>'.format(self.__tablename__)
    
# class Users(db.Model):
#     userid = db.Column(db.Integer, primary_key=True)
#     isactive = db.Column(db.Boolean)    
#     contact = db.Column(db.String(255), unique=True)

#     def __repr__(self):
#         return '<Ufarms {}>'.format(self.name)