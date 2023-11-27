from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db, map, geocoder
from app.models import Ufarms, Users
# from app.forms import SignUpForm
import random
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
    ufarms_db_table = Ufarms.query.all()

    if ufarms:
        map.get_map(ufarms_db_table)
        print('DB connection successful')
        return render_template('formatted_map.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')
    else:
        return render_template('formatted_map.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')

@app.route('/testmap', methods=['GET', 'POST'])
def show_map2():
    if request.method == 'POST':
        # Access form data using request.form
        query = request.form.get('query')
        category = request.form.get('category')
        # Now you have the user input in the 'query' and 'category' variables todo currently can only search farms category
        print('User Input - Query:', query)
        print('User Input - Category:', category)
    ufarms_db_table = Ufarms.query.all()

    if ufarms:
        coordinates = geocoder.geocode_address(query)
        print(coordinates)
        map.get_map(ufarms_db_table, coordinates, query)
        return render_template('formatted_map_copy.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')
    else:
        return render_template('formatted_map_copy.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')


# todo -- rather than implement this, maybe use cookie cutter method
@app.route('/signup', methods=['GET', 'POST'])
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
    return render_template('signup.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Email Signup')

@app.route('/about')
def about():
    return render_template('about.html', title='Ufarms - About')

@app.route('/survey')
def mailing():
    return render_template('mailinglist.html', title='Ufarms - Mailbox')

@app.route('/redirect_about')
def redirect_about():
    flashed_message = Markup('<strong>Copied to clipboard</strong>')
    flash(flashed_message)
    return redirect(url_for('about'))



# directories
@app.route('/ufarmers', methods=['GET', 'POST'])
def ufarmers():
    return render_template('ufarmers.html', title='Test Profile Directory Page')

# future route ufarmers/<hash or username>
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html', title='Test Profile Page')


#  todo findme - placeholder for futuer listed directories
@app.route('/ufarms', methods=['GET', 'POST'])
def ufarms():
    return render_template('ufarms.html', title='Test Farm Page')

@app.route('/ufarm', methods=['GET', 'POST'])
def ufarm():
    return render_template('ufarm.html', title='Test Farm Page')




# testing
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
