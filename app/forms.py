from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField
from wtforms.validators import DataRequired, Length
from wtforms import DateField, PasswordField

from app.models import Users as User
# templates for user input fields - these variables will be used to call the APIs and web scrape

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, **kwargs):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append("Unknown username")
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append("Invalid password")
            return False

        if not self.user.active:
            self.username.errors.append("User not activated")
            return False
        return True

class RegisterForm(FlaskForm):
    """Register form."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        "Verify password",
        [DataRequired(), EqualTo("password", message="Passwords must match")],
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, **kwargs):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True

class Search_Farms(FlaskForm):

    location = StringField('Address',
                        validators=[DataRequired(), Length(min=5, max=30)],
                        render_kw={'placeholder': '55555 Sleighbell St. Northpole, NP 00001'}) 
    date = DateField('Start Date', format = '%m/%d/%Y', description = 'Time',
                        render_kw={'placeholder': 'Format: mm-dd-YYYY'},
                        validators=[Length(min=10, max=10)]) 
    time_span = RadioField('Time Span', 
                        choices=[('1','1 day'),('3','3 days'), ('7', '7 days')],
                        default= '1', validators=[DataRequired()]) 
    submit = SubmitField('Look for Sites')


# class SignUpForm(FlaskForm):
#     first_name = StringField('First Name', description = 'First Name',
#         validators= [DataRequired()])
#     last_name = StringField('Last Name', description = 'First Name',
#         validators= [DataRequired()])
#     email = StringField('Email', description = 'Email',
#         validators= [DataRequired()])
#     consent = BooleanField('I want to recieve updates on the progress of Ufarms community agriculture project',
#         validators= [DataRequired()])
#     submit = SubmitField('Sign up')
#     '''
#     password = StringField('Password', description = 'At least 7 characters number and symbol',
#         validators= [])#should be a dollar ammount float/integer
#     password_confirm = StringField('Repeat Password', description = 'password confirm',
#         validators= [])#should be a dollar ammount float/integer
    
#     # Hash the user's password for security
#     hashed_password = generate_password_hash(password)
    
#     # Store the user's information in a database
#     # You will need to replace this with your own database code
#     db.insert_user(username, email, hashed_password)
#     '''
#     news_updates = RadioField('Does the utility provider charge for peak hours?',
#         description = 'sign up', choices=[('Yes', 1, "No", 0)], validators=[DataRequired()])
#     #submit = SubmitField('Submit')