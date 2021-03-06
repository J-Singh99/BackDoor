import enum
from datetime import datetime

from BackDoor import db, login_manager

from flask_login import UserMixin
from flask_appbuilder.models.mixins import ImageColumn
#from db import PrimaryKeyConstraint



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
class BRANCH(enum.Enum):
    aero = 'Aeronautical Engineering/'
    cse = 'Computer Science and Engineering'
    civil = 'Civil Engineering'
    ece = 'Electronics and Communication Engineering'
    electical = 'Electrical Engineering'
    mech = 'Mechanical Engineering'
class PROGRAM(enum.Enum):
	btech = 'B. Tech'
	mtch = 'M. Tech'
	phd = 'Ph. D'
class YEAR(enum.Enum):
	first = '1'
	second = '2'
	third = '3'
	fourth = '4'
class ADMIN_LEVEL(enum.Enum):
	level1 = 'ONE'
	level2 = 'TWO'
	level3 = 'THREE'
class DAY(enum.Enum):
	mon = 'Monday'
	tue = 'Tuesday'
	wed = 'Wednesday'
	thu = 'Thursday'
	fri = 'Friday'


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
	faculty_table = db.relationship('FacultyTable', backref='userInfo', lazy=True)
	admin_table = db.relationship('AdminTable', backref='userInfo', lazy=True)
	club_table = db.relationship('ClubTable', backref='userInfo', lazy=True)

class StudentTable(db.Model):
	__tablename__ = 'studenttable'

	#__table_args__ = ( PrimaryKeyConstraint('user_id', 'SID'),)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	SID = db.Column(db.String(8), primary_key=True, unique=True, nullable=False)
	branch = db.Column(db.Enum(BRANCH), nullable=False)
	program = db. Column(db.Enum(PROGRAM), nullable=False)
	year = db.Column(db.Enum(YEAR), default=YEAR.first, nullable=False)

class FacultyTable(db.Model):
	__tablename__ = 'facultytable' 
	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
#	enrol = db.relationship('Enrol', backref='enrolling_faculty', lazy=True)

	FID = db.Column(db.String(8), primary_key=True, unique=True, nullable=False)
	branch = db.Column(db.Enum(BRANCH), nullable=False)
	position = db.Column(db.String(50), nullable = True)

class AdminTable(db.Model):
	__tablename__ = 'admintable' 
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	EID = db.Column(db.String(8), primary_key=True, unique=True, nullable=False)
	position = db.Column(db.String(50), nullable = True)
	admin_level = db.Column(db.Enum(ADMIN_LEVEL), nullable=True)
	
class ClubTable(db.Model):
	__tablename__ = 'clubtable'
	
	#The User would just be the Prof. in charge of the Club#
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	CID = db.Column(db.String(8), primary_key=True, unique=True, nullable=False)
	
class Course(db.Model):
	__tablename__ = 'course'
#	enrol_info = db.relationship('Enrol', backref='enroled_course', lazy=True)

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True, nullable=True)
	code = db.Column(db.String(6), primary_key=True, unique=True, nullable=False)
	credits = db.Column(db.Integer, unique=False, nullable=True)
	LTP = db.Column(db.String(3), unique=False, nullable=True)
	objectives = db.Column(db.String(500), unique=False, nullable=True)
	profsIDs = db.Column(db.String(27), unique=False, nullable=False)
	tot_classes = db.Column(db.Integer, unique=False, nullable=False)

class Enrol(db.Model):
	__tablename__ = 'enrol'
	fac_id = db.Column(db.Integer, db.ForeignKey('facultytable.FID'), nullable=False)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)  
	
	id = db.Column(db.Integer, primary_key=True)
	branch = db.Column(db.Enum(BRANCH), nullable=False)
	program = db. Column(db.Enum(PROGRAM), nullable=False)
	year = db.Column(db.Enum(YEAR), default=YEAR.first, nullable=False)
		

class Assessments(db.Model):
	__tablename__ = 'assessments'
	
	id = db.Column(db.Integer, primary_key=True)
	sub_code = db.Column(db.String(6), unique=False, nullable=False)
'''
	type_
	points 	
	branch
	program
	year
	name
	description	
'''

class TimeTable(db.Model):
	__tablename__ = 'timetable'

	id = db.Column(db.Integer, primary_key=True)
	branch = db.Column(db.Enum(BRANCH), nullable=False)
	program = db. Column(db.Enum(PROGRAM), nullable=False)
	year = db.Column(db.Enum(YEAR), default=YEAR.first, nullable=False)
	day = db.Column(db.Enum(DAY), nullable=False)
	slot1 = db.Column(db.String(30), default=None, nullable=True)
	slot2 = db.Column(db.String(30), default=None, nullable=True)
	slot3 = db.Column(db.String(30), default=None, nullable=True)
	slot4 = db.Column(db.String(30), default=None, nullable=True)
	slot5 = db.Column(db.String(30), default=None, nullable=True)
	slot6 = db.Column(db.String(30), default=None, nullable=True)
	slot7 = db.Column(db.String(30), default=None, nullable=True)
	slot8 = db.Column(db.String(30), default=None, nullable=True)
	slot9 = db.Column(db.String(30), default=None, nullable=True)
	slot10 = db.Column(db.String(30), default=None, nullable=True)


'''
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
'''