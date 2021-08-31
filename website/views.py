from flask import Blueprint, flash
from flask import Flask, redirect, url_for, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Subjects, Comments

views = Blueprint('views', __name__)


@views.route("/")
def welcome():
	#if current_user.is_authenticated:
		#return "<h1>Welcome to Online Class<h1>"
	return render_template("index.html")

@views.route("/student_home")
@login_required
def student_home():
	subjects = Subjects.query.all()
	return render_template("student_homepage.html", subjects= subjects)

@views.route("/teacher_home")
@login_required
def teacher_home():	
	subjects = Subjects.query.all()
	return render_template("teacher_homepage.html", subjects= subjects)

@views.route("/profile")
@login_required
def profile():
	user = current_user
	return render_template("profile.html", user=user)

@views.route("/video")
@login_required
def video():
	user = current_user
	return render_template("video.html", user=user)

@views.route("/subject_addition", methods=['GET', 'POST'])
@login_required
def add_subject():
	teachers = User.query.filter_by(rights='Teacher')
	if current_user in teachers:
		if request.method=='POST':
			subject = request.form.get('subject')
			credits = request.form.get('credits')
			semester = request.form.get('semester')

			new_sub = Subjects(name=subject, credits=credits,semester=semester, user_id=current_user.id)
			db.session.add(new_sub)
			db.session.commit()
			flash('New Subject Added!', category='success')
			return redirect(url_for('views.teacher_home'))
		return render_template("subject_addition.html", user=current_user)
	else:
		flash("You do not have access", category=error)
		return render_template("student_homepage.html", user=current_user)