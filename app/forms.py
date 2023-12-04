from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, DateField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import Users
from app import bcrypt
# templates for user input fields - these variables will be used to call the APIs and web scrape

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, **kwargs):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = Users.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append("Unknown username")
            return False

        # bcrypt.check_password_hash
        return True

class RegisterForm(FlaskForm):
    """Register form."""

    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=40)])
    confirm_password = PasswordField(
        "Confirm Password",
        [DataRequired(), EqualTo("password", message="Passwords must match")],
    )
    submit = SubmitField("Register")

    def validate(self, **kwargs):
        """Validate the form."""
        if not super().validate(**kwargs):
            return False
        user = Users.query.filter_by(Username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = Users.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        # Update the user model with hashed password
        self.user = Users(
            Username=self.username.data,
            Email=self.email.data,
            password=bcrypt.generate_password_hash(self.password.data),
        )
        return True

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

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