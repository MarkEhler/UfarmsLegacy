from flask import render_template, flash, redirect, url_for, request, Response, session
from app import app
#from app.forms import SimForm
#from app.api_calls import *
#import os, io, json


@app.route('/')
@app.route('/dashboard', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Welcome to Ufarms - Community Agriculture Project')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the user's input from the signup form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Hash the user's password for security
        hashed_password = generate_password_hash(password)
        
        # Store the user's information in a database
        # You will need to replace this with your own database code
        db.insert_user(username, email, hashed_password)
        
        # Redirect the user to the login page after signup
        return redirect(url_for('login'))
    
    # Render the signup page template for GET requests
    return render_template('signup.html')

@app.route('/about')
def about():
	return render_template('about.html', title='About')
