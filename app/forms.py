from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField
from wtforms.validators import DataRequired, Length
from wtforms import DateField

# templates for user input fields - these variables will be used to call the APIs and web scrape

class SimForm(FlaskForm):

    location = StringField('Address',
                        validators=[DataRequired(), Length(min=5, max=30)],
                        render_kw={'placeholder': '55555 Sleighbell St. Northpole, NP 00001'}) 
    date = DateField('Start Date', format = '%m/%d/%Y', description = 'Time',
                        render_kw={'placeholder': 'Format: mm-dd-YYYY'},
                        validators=[Length(min=10, max=10)]) 
    time_span = RadioField('Time Span', 
                        choices=[('1','1 day'),('3','3 days'), ('7', '7 days')],
                        default= '1', validators=[DataRequired()]) 
    submit = SubmitField('Run Simulation')

    # def validate_form(self, zipcode, date):
    # 	if zipcode.data != int:
    # 		raise ValidationError('Please use a valid zipcode')
    	# if date.data > datetime.datetime.now():
    	# 	raise ValidationError('')

class StaticForm(FlaskForm):
# static info will also use latitude to calculate the tilt angle when displaying info
    bill = StringField('Average monthly energy bill?', description = 'dollar ammount',
        validators= [])#should be a dollar ammount float/integer

    peak_hours = RadioField('Does the utility provider charge for peak hours?',
        description = 'peak hours', choices=[('Yes', 1, "No", 0)], validators=[DataRequired()])

    time_zone = StringField('Timezone', description='GMT+/-',
        validators=[Length(min=2, max=3)],
        render_kw={'placeholder': '-4 for EST, -6 for MST'})

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', description = 'First Name',
        validators= [DataRequired()])
    last_name = StringField('Last Name', description = 'First Name',
        validators= [DataRequired()])
    email = StringField('Email', description = 'Email',
        validators= [DataRequired()])
    consent = BooleanField('I want to recieve updates on the progress of Ufarms community agriculture project',
        validators= [DataRequired()])
    submit = SubmitField('Sign up')
    '''
    password = StringField('Password', description = 'At least 7 characters number and symbol',
        validators= [])#should be a dollar ammount float/integer
    password_confirm = StringField('Repeat Password', description = 'password confirm',
        validators= [])#should be a dollar ammount float/integer
    
    # Hash the user's password for security
    hashed_password = generate_password_hash(password)
    
    # Store the user's information in a database
    # You will need to replace this with your own database code
    db.insert_user(username, email, hashed_password)
    '''
    news_updates = RadioField('Does the utility provider charge for peak hours?',
        description = 'sign up', choices=[('Yes', 1, "No", 0)], validators=[DataRequired()])
    #submit = SubmitField('Submit')