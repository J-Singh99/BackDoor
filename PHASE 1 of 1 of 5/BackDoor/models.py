import enum
from datetime import datetime

from BackDoor import db, login_manager

from flask_login import UserMixin
from flask_appbuilder.models.mixins import ImageColumn


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class GENDER(enum.Enum):
    male = 'M'
    female = 'F'
    retard = 'R'
class GROUP(enum.Enum):
    student = 'S'
    faculty = 'F'
    admin = 'A'
    club = 'C'

class User(db.Model, UserMixin):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	first_name = db.Column(db.String(25), unique=False, nullable=False)
	middle_name = db.Column(db.String(25), unique=False, nullable=True)
	last_name = db.Column(db.String(25), unique=False, nullable=True)
	DOB = db.Column(db.DateTime, unique=False, nullable=True)
	gender = db.Column(db.Enum(GENDER), default=GENDER.retard, nullable=False)
	user_group = db.Column(db.Enum(GROUP), default=GROUP.student, nullable=False)

	student_table = db.relationship('StudentTable', backref='userInfo', lazy=True)
	faculty_table = db.relationship('StudentTable', backref='userInfo', lazy=True)
	admin_table = db.relationship('StudentTable', backref='userInfo', lazy=True)
	club_table = db.relationship('StudentTable', backref='userInfo', lazy=True)


	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



	overtimgInfo = db.relationship('InputInformation', backref='hidder', lazy=True)
	revealimgInfo = db.relationship('CovertInput', backref='revealer', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class InputInformation(db.Model):
	__tablename__ = 'inputinformation'

	id = db.Column(db.Integer, primary_key = True)
	inputImage = db.Column(db.String(20), nullable=False, default='default.jpg')
	typeStego = db.Column(db.String(3), default='TXT', nullable=False)
	hideImg = db.Column(db.String(20), default='default.jpg')
	hideText = db.Column(db.String(50), default='Jaspreet is the greatest!')
	lsb = db.Column(db.Integer(), nullable=False)
	fileName = db.Column(db.String(20))

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	final_stego = db.relationship('Final_Stego', uselist=False, backref='mainInfo', lazy=True)

	def __repr__(self):
		return f"ID:'{self.id}', LSB:'{self.lsb}', File Name:'{self.fileName}')"


class Final_Stego(db.Model):
	__tablename__ = 'final_stego'
	id = db.Column(db.Integer, primary_key=True)
	covertImg = db.Column(db.String(20), nullable=False)
	
	overtImgID = db.Column(db.Integer, db.ForeignKey('inputinformation.id'), unique=True, nullable=False)
