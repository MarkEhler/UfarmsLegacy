from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db, map, geocoder, forms, bcrypt
from app.models import Ufarms, Users
from werkzeug.utils import secure_filename
from config import Config
from markupsafe import Markup



@app.route('/')
def index():
    app_directory = app.root_path
    return render_template('home.html', template_folder=Config.TEMPLATE_PATH, title='Welcome to Ufarms - Community Agriculture Project')

@app.route('/home', methods=['GET', 'POST'])
def home():    
    return render_template('home.html', template_folder=Config.TEMPLATE_PATH, title='Welcome to Ufarms - Community Agriculture Project')


@app.route('/login', methods=['GET', 'POST'])
# todo create a/b for if user is tied to an active user session or is acting as a public user
# large effort as it requires adding session knowledge to site
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Hash the user's password for security
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')  # Decode the bytes to string

        # Create a new user instance with the form data
        new_user = Users(
            Username=username,
            Email=email,
            password=hashed_password
        )
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Redirect the user to the login page after signup
        flash(f'Let\'s grow together, {username}')
        return redirect(url_for('welcome', username=username))
    
    return render_template('login.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Email Signup', form=form)

@app.route('/welcome/<username>', methods=['GET', 'POST'])
def welcome(username):
    form = forms.ProfileForm()

    if form.validate_on_submit():
        # Update the user with additional information
        user = Users.query.filter_by(Username=username).first_or_404()
        user.Fname = form.fname.data
        user.Lname = form.lname.data
        user.Bio = form.bio.data

        # Handle profile picture upload
        # todo pics in database? the below section needs reworking
        if form.profile_pic.data:
            # Save the uploaded file to a designated folder
            filename = secure_filename(form.profile_pic.data.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.profile_pic.data.save(file_path)
            user.ProfilePic = file_path
        
        db.session.commit()

        return redirect(url_for('user_profile', username=username))

    return render_template('welcome.html', form=form)

# for demoing the map.  loads in burlington with the initial canned data
# and for a default display location should the test map fail
@app.route('/map', methods=['GET', 'POST'])
def show_map():
    ufarms_db_table = Ufarms.query.all()

    if ufarms:
        map.get_map(ufarms_db_table)
        print('DB connection successful')
        return render_template('formatted_map.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')
    else:
        return render_template('formatted_map.html', template_folder=Config.TEMPLATE_PATH, title='Ufarms - Community Agriculture Map')

# for testing the search function
# the route where all future development should go for
# n - nearest farm node display
# 
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
@app.route('/ufarmers/<username>')
def user_profile(username):
    user = Users.query.filter_by(Username=username).first_or_404()
    return render_template('profile.html', user=user)


#  todo findme - placeholder for futuer listed directories
@app.route('/ufarms', methods=['GET', 'POST'])
def ufarms():
    return render_template('ufarms.html', title='Test Farm Page')

# todo findme - placeholder for futer farms profile page
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