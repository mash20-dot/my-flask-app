from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#database structure
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindspace.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    firstname = db.Column(db.String(50),)
    lastname = db.Column(db.String(50),)
    email = db.Column(db.String(150), unique=True,)
    password = db.Column(db.String(150),)










