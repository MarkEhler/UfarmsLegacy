from server import db, bcrypt
from sqlalchemy import Column 
from django.db import models
import string, random
from sqlalchemy.ext.hybrid import hybrid_property

## used by cookiecutter app
# from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
# from app.database import Column, PkModel, db, reference_col, relationship
from server import bcrypt

class UserManager(models.Manager):
    def generate_public_id(self, size=12, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create_user_with_public_id(self, name):
        user = self.create(name=name, PublicID=self.generate_public_id())
        return user


class Ufarms(db.Model):
    """A host farm on the app."""

    __tablename__ = 'Ufarms'
    UfarmID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PublicFarmID = db.Column(db.String(12), unique=True, nullable=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=True)
    FarmName = db.Column(db.String(25), unique=True)
    FarmDescription = db.Column(db.String(255), default=None, nullable=True)
    IsActive = db.Column(db.Boolean)
    AddressStr = db.Column(db.String(255), unique=True)
    IsOwner = db.Column(db.Boolean, default=None, nullable=True)
    Email = db.Column(db.String(255), unique=True, default=None, nullable=True)
    Request = db.Column(db.String(255), default=None, nullable=True)
    Privacy_lat = db.Column(db.Float, default=None, nullable=True)
    Privacy_lon = db.Column(db.Float, default=None, nullable=True)
    CreatedAt = db.Column(db.DateTime, server_default=db.func.now())
    UpdatedAt = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    SunExposure = db.Column(db.Integer, default=None, nullable=True)
    WaterSource = db.Column(db.Integer, default=None, nullable=True)
    HardinessZone = db.Column(db.Float, default=None, nullable=True)
    Parking = db.Column(db.String(8), default=None, nullable=True)
    PlaidID = db.Column(db.String(25), default=None, nullable=True)
    FarmPhoto = db.Column(db.LargeBinary, default=None, nullable=True)

    # Define the relationship with the Users table
    user = db.relationship('Users', backref='ufarms')

    objects = UserManager()
    def __init__(self, *args, **kwargs):
        super(Ufarms, self).__init__(*args, **kwargs)
        if not self.PublicFarmID:
            self.PublicFarmID = self.objects.generate_public_id()

    def serialize(self):
        return {
            'UfarmID': self.UfarmID,
            'PublicFarmID': self.PublicFarmID,
            'UserID': self.UserID,
            'FarmName': self.FarmName,
            'FarmDescription': self.FarmDescription,
            'IsActive': self.IsActive,
            'AddressStr': self.AddressStr,
            'IsOwner': self.IsOwner,
            'Email': self.Email,
            'Request': self.Request,
            'Privacy_lat': self.Privacy_lat,
            'Privacy_lon': self.Privacy_lon,
            'CreatedAt': self.CreatedAt,
            'UpdatedAt': self.UpdatedAt,
            'SunExposure': self.SunExposure,
            'WaterSource': self.WaterSource,
            'HardinessZone': self.HardinessZone,
            'Parking': self.Parking,
            'PlaidID': self.PlaidID,
            'FarmPhoto': self.FarmPhoto
        }

    objects = UserManager()
    def __init__(self, *args, **kwargs):
        super(Ufarms, self).__init__(*args, **kwargs)
        if not self.PublicFarmID:
            self.PublicFarmID = self.objects.generate_public_id()


    def serialize(self):
        return {
            'UfarmID': self.UfarmID,
            'PublicFarmID': self.PublicFarmID,
            'UserID': self.UserID,
            'FarmName': self.FarmName,
            'IsActive': self.IsActive,
            'AddressStr': self.AddressStr,
            'Contact': self.Contact,
            'Request': self.Request,
            'Privacy_lat': self.Privacy_lat,
            'Privacy_lon': self.Privacy_lon,
            'CreatedAt': self.CreatedAt,
            'UpdatedAt': self.UpdatedAt
        }
    
    def __repr__(self):
        return '<Users {}>'.format(self.__tablename__)

class Users(db.Model):
    """A farmer."""

    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PublicID = db.Column(db.String(12), unique=True, nullable=True)
    Username = db.Column(db.String(30), unique=True)
    Fname = db.Column(db.String(30), nullable=True)
    Lname = db.Column(db.String(30), nullable=True)
    _password = db.Column("password", db.LargeBinary(128), nullable=True)
    IsActive = db.Column(db.Boolean, default=True)
    AddressStr = db.Column(db.String(255), unique=True)
    Email = db.Column(db.String(255), unique=True)
    Bio = db.Column(db.String(255), unique=True, nullable=True)
    IsHost = db.Column(db.Boolean(), default=False)
    IsAdmin = db.Column(db.Boolean(), default=False)
    ProfilePic = db.Column(db.String(255), unique=True, nullable=True)
    CreatedAt = db.Column(db.DateTime, server_default=db.func.now())
    UpdatedAt = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    Carrots = db.Column(db.Integer, default=3)
    Exp = db.Column(db.Integer, default=1)
    StripeID = db.Column(db.String(25), unique=True, nullable=True)


    def serialize(self):
        return {
            'UserID': self.UserID,
            'PublicID': self.PublicID,
            'Username': self.Username,
            'Fname': self.Fname,
            'Lname': self.Lname,
            'password': self.password,
            'IsActive': self.IsActive,
            'AddressStr': self.AddressStr,
            'Email': self.Email,
            'Bio': self.Bio,
            'IsHost': self.IsHost,
            'IsAdmin': self.IsAdmin,
            'StripeID': self.StripeID,
            'ProfilePic': self.ProfilePic,
            'Carrots': self.Carrots,
            'Exp': self.Exp,
            'CreatedAt': self.CreatedAt,
            'UpdatedAt': self.UpdatedAt
        }


    objects = UserManager()

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        if not self.PublicID:
            self.PublicID = self.objects.generate_public_id()

    def serialize(self):
        return {
            'UserID': self.UserID,
            'PublicID': self.PublicID,
            'Username': self.Username,
            'Fname': self.Fname,
            'Lname': self.Lname,
            'password': self.password,
            'IsActive': self.IsActive,
            'AddressStr': self.AddressStr,
            'Email': self.Email,
            'Bio': self.Bio,
            'IsHost': self.IsHost,
            'CreatedAt': self.CreatedAt,
            'UpdatedAt': self.UpdatedAt
        }

    def __repr__(self):
        return '<Users {}>'.format(self.__tablename__)
    
    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password
    
    def get_profile_url(self):
        return f"/profile/{self.Username}"

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.Fname} {self.Lname}"