from app import db
from sqlalchemy import Column 
from django.db import models
import string
import random
## used by cookiecutter app
# from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
# from app.database import Column, PkModel, db, reference_col, relationship
from app import bcrypt

class UserManager(models.Manager):
    def generate_public_id(self, size=12, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create_user_with_public_id(self, name):
        user = self.create(name=name, PublicID=self.generate_public_id())
        return user
    
class Ufarms(db.Model):
    """A host location on the app."""

    __tablename__ = 'Ufarms'
    UfarmID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PublicFarmID = db.Column(db.String(12), unique=True, nullable=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=True) #foreign keys not supported on planet scale.  users is parent table.
    FarmName = db.Column(db.String(255), unique=True)
    IsActive = db.Column(db.Boolean)
    AddressStr = db.Column(db.String(255), unique=True)
    Contact = db.Column(db.String(255), unique=True)
    Request = db.Column(db.String(255))
    Privacy_lat = db.Column(db.Float)
    Privacy_lon = db.Column(db.Float)
    CreatedAt = db.Column(db.DateTime, server_default=db.func.now())
    UpdatedAt = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.PublicFarmID:
            self.PublicFarmID = self.objects.generate_public_id()
        super().save(*args, **kwargs)

    def serialize(self):
        return {
            'UfarmID': self.UfarmID,
            'PublicFarmID': self.PublicFarmID,
            'UserID': self.UserID,
            'FarmName': self.Name,
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
    """A user of the app."""

    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PublicID = db.Column(db.String(12), unique=True, nullable=True)
    Username = db.Column(db.String(30), unique=True)
    FirstName = Column(db.String(30), nullable=True)
    LastName = Column(db.String(30), nullable=True)
    _password = Column("password", db.LargeBinary(128), nullable=True)
    IsActive = db.Column(db.Boolean, default=True)
    AddressStr = db.Column(db.String(255), unique=True)
    Email = db.Column(db.String(255), unique=True)
    Host = db.Column(db.Boolean, default=False)
    Bio = db.Column(db.String(255), unique=True, nullable=True)
    CreatedAt = db.Column(db.DateTime, server_default=db.func.now())
    UpdatedAt = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    IsAdmin = Column(db.Boolean(), default=False)

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.PublicID:
            self.PublicID = self.objects.generate_public_id()
        super().save(*args, **kwargs)

    def serialize(self):
        return {
            'UserID': self.UserID,
            'PublicID': self.PublicID,
            'Name': self.Name,
            'IsActive': self.IsActive,
            'AddressStr': self.AddressStr,
            'Email': self.Contact,
            'Host': self.Host,
            'Bio': self.Bio,
            'CreatedAt': self.CreatedAt,
            'UpdatedAt': self.UpdatedAt
        }

    def __repr__(self):
        return '<Users {}>'.format(self.__tablename__)
    
    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self._password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"