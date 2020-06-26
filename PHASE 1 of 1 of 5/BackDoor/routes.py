from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

import secrets, os

from PIL import Image
import PIL, numpy

# FORMS
#from steganographer.forms import RegistrationForm, LoginForm, UpdateAccountForm, StegoHide, StegoReveal

# MODELS
#from steganographer.models import User, InputInformation, Final_Stego, CovertInput, RevealedInfo 


# ERRORS
@app.errorhandler(404)
def error_404(error):
    return render_template('404.html', title='Error 404'), 404
@app.errorhandler(403)
def error_403(error):
    return render_template('403.html', title='Error 403'), 403
@app.errorhandler(500)
def error_500(error):
    return render_template('500.html', title='Error 500'), 500



# ROUTES

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

'''
@app.route('/test')
def test():
	return render_template('500.html',title = 'TEST!!!!')



@app.route('/register', methods = ['GET', 'POST'])
def register():

	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	form = RegistrationForm()
	
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created!!\nYou can now log in!!', 'success')
		return redirect(url_for('login'))
	
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	form = LoginForm()
	
	if form.validate_on_submit():	
		user = User.query.filter_by(email = form.email.data).first()
		
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember = form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))

		else:
			flash('Login Unsuccessful!!\nPlease check email and password!!', 'danger')
	return render_template('login.html', title='Login', form=form)



@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/profile/<string:username>')
@login_required
def profile(username):
	user = User.query.filter_by(username=username).first_or_404()
	
	hide_list = []
	HIDES = InputInformation.query.filter_by(hidder=user)
	for pic in HIDES:
		hide_list.append(Final_Stego.query.filter_by(mainInfo=pic).first())
	
	
	return render_template('profile.html', user=user, HIDES=HIDES, 
							hide_list=hide_list)
'''