from flask import Flask, render_template, request, redirect, session, flash
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
		return redirect('/')
app.run(debug=True)