from app import db

class Ufarms(db.Model):
    __tablename__ = 'Ufarms'
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
    
class Users(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), unique=True)
    IsActive = db.Column(db.Boolean)    
    Contact = db.Column(db.String(255), unique=True)
    Bio = db.Column(db.String(255), unique=True)
    StartDate = db.Column(db.Float)

    # def serialize(self):
    #     return {
    #     }

    def __repr__(self):
        return '<Users {}>'.format(self.__tablename__)