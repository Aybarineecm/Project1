from . import db #ask sir what this does
from flask import Flask, request

app= Flask(__name__)
class Properties(db.Model):

     __tablename__ = 'properties'

     propertyid = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(180),nullable=False)
     location = db.Column(db.String(280),nullable=False)
     bathnum = db.Column(db.Integer,nullable=False)
     bednum = db.Column(db.Integer,nullable=False)
     price = db.Column(db.Integer,nullable=False)
     proptype = db.Column(db.String(15))
     descr = db.Column(db.String(800))
     photo= db.Column(db.Text,nullable=False)


     def __init__(self,title, location,bathnum,bednum, price,proptype,descr,photo):
         self.title = title 
         self.location = location
         self.bathnum = bathnum
         self.bednum = bednum
         self.price = price  
         self.proptype = proptype
         self.photo= photo
         self.descr = descr