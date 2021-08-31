from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Subjects(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150))
	credits = db.Column(db.Integer)
	semester = db.Column(db.Integer) 
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.String(10000))
	date = db.Column(db.DateTime(timezone=True), default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	name = db.Column(db.String(150))
	college = db.Column(db.String(150))
	dept = db.Column(db.String(150))
	comments = db.relationship('Comments')
	roll_no = db.Column(db.String(150))
	acad_year = db.Column(db.String(150))
	gender = db.Column(db.String(150))
	age = db.Column(db.String(150))
	blood = db.Column(db.String(150))
	rights = db.Column(db.String(150))












