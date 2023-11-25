from app import db
from django.db import models
import string
import random

class UserManager(models.Manager):
    def generate_public_id(self, size=12, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create_user_with_public_id(self, name):
        user = self.create(name=name, public_id=self.generate_public_id())
        return user
    
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

    # def serialize(self):
    #     return {
    #     }

    def __repr__(self):
        return '<Users {}>'.format(self.__tablename__)
    
# class User(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     public_id = models.CharField(max_length=12, unique=True, blank=True, null=True)
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     def save(self, *args, **kwargs):
#         if not self.public_id:
#             self.public_id = self.objects.generate_public_id()
#         super().save(*args, **kwargs)