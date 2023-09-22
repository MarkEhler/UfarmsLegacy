from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db, map
from app.models import Ufarms
# from app.forms import SignUpForm
import os, io, json, random
from config import Config
from markupsafe import Markup



@app.route('/')
def index():
    app_directory = app.root_path
    return render_template('home.html', template_folder=Config.TEMPLATE_PATH, title='Welcome to Ufarms - Community Agriculture Project')

@app.route('/home', methods=['GET', 'POST'])
def home():    
    return render_template('home.html', template_folder=Config.TEMPLATE_PATH, title='Welcome to Ufarms - Community Agriculture Project')

@app.route('/map', methods=['GET', 'POST'])
def show_map():
    ufarms = Ufarms.query.all()

    if ufarms:
        map.get_map(ufarms)
        print('DB connection successful')
        return render_template('formatted_map.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')
    else:
        return render_template('formatted_map.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')

# todo -- rather than implement this, maybe use cookie cutter method
# @app.route('/signup', methods=['GET', 'POST'])
# def survey():
#     form = SignUpForm()
#     if form.validate_on_submit():
#         first_name = form['first_name']
#         last_name = form['last_name']
#         email = form['email']
        
#         # Hash the user's password for security
#         #hashed_password = generate_password_hash(password)
        
#         # Store the user's information in a database
#         # You will need to replace this with your own database code
#         # db.insert_user(username, email, hashed_password)
        
#         # Redirect the user to the login page after signup
        
#         flash(f'Let\'s grow together, {form.first_name}')
#         return redirect(url_for('home'))
    
#     # Render the signup page template for GET requests
#     return render_template('signup.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Email Signup')

@app.route('/about')
def about():
    return render_template('about.html', title='Ufarms - About')

@app.route('/survey')
def mailing():
    rand_int = random.randint(1, 2) #todo create a counter that counts to 18 before directing all traffic to the google
    #flash('email copied to clipboard')
    if rand_int == 1:
        return redirect(url_for('mailing2'))
    else:
    	return render_template('mailinglist.html', title='Ufarms - Mailbox')

@app.route('/mailing2')
def mailing2():
    #flash('email copied to clipboard')
    return render_template('mailinglist2.html', title='Ufarms - Mailbox')

# future route ufarmer/<hash or username>
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html', title='Test Profile Page')

@app.route('/redirect_about')
def redirect_about():
    flashed_message = Markup('<strong>Copied to clipboard</strong>')
    flash(flashed_message)
    return redirect(url_for('about'))

@app.route('/iframe')
def iframe():
    return render_template('iframe.html')

@app.route('/iframe_content')
def iframe_content():
    return render_template('iframe_content.html')

@app.route('/db_test', methods=['GET'])
def db_test():
    ufarms = Ufarms.query.all()
    # print('printing db cnx debug')
    # print(ufarms)
    # return jsonify([item.serialize() for item in ufarms])
    return render_template('db_test.html', ufarms=ufarms)
