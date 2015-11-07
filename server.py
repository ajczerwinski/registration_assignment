from flask import Flask, render_template, request, redirect, session, flash
import re
import time
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
PASSWORD_CHECKER = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
BIRTHDATE_CHECKER = re.compile(r'(\d{4}/\d{2}/\d{2})')
todays_date = "2015/11/07"
compare_date = time.strptime(todays_date, "%Y/%m/%d")
app = Flask(__name__)
app.secret_key="SecretKeyMePls"
@app.route('/')
def index():
	return render_template('index.html')
@app.route("/process", methods=["POST"])
def submit():
	if request.method =="POST":
		session['email'] = request.form['email']
		session['first_name'] = request.form['first_name']
		session['last_name'] = request.form['last_name']
		session['birth_date'] = request.form['birth_date']
		user_date = time.strptime(session['birth_date'], "%Y/%m/%d")
		session['password'] = request.form['password']
		session['confirm_password'] = request.form['confirm_password']
		# Verifies that all fields are required and must not be blank
		if len(session['email']) < 1 or len(session['first_name']) < 1 or len(session['last_name']) < 1 or len(session['birth_date']) < 1 or len(session['password']) < 1 or len(session['confirm_password']) < 1:
			flash("No fields can be empty!")
			return redirect('/')
		# Verifies that First and Last Name cannot contain any numbers
		elif not session['first_name'].isalpha() or not session['last_name'].isalpha():
			flash("First and Last name must contain only letters!")
			return redirect('/')
		# Verifies that Password is more than 8 characters
		elif len(session['password']) < 9:
			flash("Password must have more than 8 characters!")
			return redirect('/')
		# Checks to verify that email is in the correct email address format
		elif not EMAIL_REGEX.match(session['email']):
			flash("Invalid Email Address!")
			return redirect('/')
		# Verifies that Password matches Confirm Password
		elif session['password'] != session['confirm_password']:
			flash("Password does not match Password Confirmation!")
			return redirect('/')
		elif not PASSWORD_CHECKER.match(session['password']):
			flash("Password must contain at least one uppercase letter and 1 number!")
			return redirect('/')
		elif not BIRTHDATE_CHECKER.match(session['birth_date']):
			flash("Birthdate appears to be in the wrong format. Make sure you're using 'yyyy/mm/dd' please!")
			return redirect('/')
		elif user_date > compare_date:
			flash("Birthdate has to be in the past!")
			return redirect('/')
		# Thanks user for submitting their information	
		else:
			flash("Thanks for submitting your information!")
			return redirect('/')
app.run(debug=True)