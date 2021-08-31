from flask import Blueprint, flash, redirect, url_for
from flask import Flask, redirect, url_for, render_template, request
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		rights = request.form.get('rights')

		user = User.query.filter_by(email=email).first()
		if user:
			if check_password_hash(user.password, password):
				flash('Logged in successfully!', category='success')
				login_user(user, remember=True)
				if user.rights == 'Student':
					return redirect('/student_home')
				elif user.rights == 'Teacher':
					return redirect('/teacher_home')
			else:
				flash('Incorrect password, try again.', category='error')
		else:
			flash('Email does not exist.', category='error')

	return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
	logout_user()
	#flash('Logged out', category='error')
	return redirect(url_for('views.welcome'))

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
	if request.method == "POST":
		post = request.form.get('id')
		email = request.form.get('email')
		name = request.form.get('name')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		college = request.form.get('college')
		department = request.form.get('dept')
		roll_no = request.form.get('roll_no')
		rights = request.form.get('rights')
		age = request.form.get('age')
		acad_year = request.form.get('acad_year')
		blood = request.form.get('blood')
		gender= request.form.get('gender')



		user = User.query.filter_by(email = email).first()
		if user :
			flash('Email already exists.', category='error')
		elif len(email) < 4:
			flash('Email must be greater than 3 characters.', category='error')
		elif len(name) < 2:
			flash('Name must be greater than 1 character.', category='error')
		elif password1 != password2:
			flash('Passwords dont match.', category='error')
		elif len(password1) < 7:
			flash('Password must be at least 7 characters.', category='error')
		else:
			new_user = User(email=email, name=name, password=generate_password_hash(
				password1, method='sha256'), college=college, dept=department, roll_no=roll_no,age=age, gender=gender,blood=blood,acad_year=acad_year,  rights=rights)
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember=True)
			flash('Account created!', category='success')
			if rights=='Student':
				return redirect(url_for('views.student_home'))
			else:
				return redirect(url_for('views.teacher_home'))

	return render_template("signup.html", boolean=True)