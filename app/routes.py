from flask import render_template, flash, redirect, url_for, request, Response, session, Flask
from app import app
from werkzeug.security import generate_password_hash
from app.forms import SignUpForm
from app.map import get_map
#from app.api_calls import *
import os, io, json, random
import settings


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', template_folder=settings.TEMPLATE_PATH, title='Welcome to Ufarms - Community Agriculture Project')

@app.route('/map')
def map():
    get_map(settings.DATA_PATH)
    return render_template('map.html', template_folder=settings.TEMPLATE_PATH, title='Welcome to Ufarms - Community Agriculture Project')
     
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']
        
        # Hash the user's password for security
        #hashed_password = generate_password_hash(password)
        
        # Store the user's information in a database
        # You will need to replace this with your own database code
        # db.insert_user(username, email, hashed_password)
        
        # Redirect the user to the login page after signup
        
        flash(f'Let\'s grow together, {form.first_name}')
        return redirect(url_for('home'))
    
    # Render the signup page template for GET requests
    return render_template('signup.html', template_folder=settings.TEMPLATE_PATH, title='Email Signup')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/contact')
def contact():
	return render_template('contact.html', title='Contact')

@app.route('/mailing')
def mailing():
    rand_int = random.randint(1, 2) #todo create a counter that counts to 18 before directing all traffic to the google
    if rand_int == 1:
        return redirect(url_for('mailing2'))
    else:
    	return render_template('mailinglist.html', title='Mailbox')

@app.route('/mailing2')
def mailing2():
	return render_template('mailinglist2.html', title='Mailbox')

@app.route('/thankyou')
def thankyou():
	return render_template('submit_confirm.html', title='Email Recieved')
