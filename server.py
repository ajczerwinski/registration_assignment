from flask import Flask, render_template, request, redirect, session, flash
import re
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
		session['password'] = request.form['password']
		session['confirm_password'] = request.form['confirm_password']
		# Validates that all fields are required and must not be blank
		if len(session['email']) < 1 or len(session['first_name']) < 1 or len(session['last_name']) < 1 or len(session['password']) < 1 or len(session['confirm_password']) < 1:
			flash("No fields can be empty!")
			return redirect('/')
		# Validates that First and Last Name cannot contain any numbers
		elif not session['first_name'].isalpha() or not session['last_name'].isalpha():
			flash("First and Last name must contain only letters!")
		return redirect('/')
app.run(debug=True)