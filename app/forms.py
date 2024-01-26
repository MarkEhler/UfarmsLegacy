# from flask import redirect
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
# from wtforms import StringField, SubmitField, RadioField, DateField, PasswordField, TextAreaField
# from wtforms.validators import DataRequired, Length, EqualTo, Email
# from app.models import Users
# from app import bcrypt
# # templates for user input fields - these variables will be used to call the APIs and web scrape

# class LoginForm(FlaskForm):
#     """Login form."""

#     username = StringField("Username", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     # email = StringField("Email", validators=[DataRequired()])

#     def __init__(self, *args, **kwargs):
#         """Create instance."""
#         super(LoginForm, self).__init__(*args, **kwargs)
#         self.user = None

#     def validate(self, **kwargs):
#         """Validate the form."""
#         initial_validation = super(LoginForm, self).validate()
#         if not initial_validation:
#             return False

#         self.user = Users.query.filter_by(username=self.username.data).first()
#         if not self.user:
#             self.username.errors.append("Unknown username")
#             return False

#         # bcrypt.check_password_hash todo

#         # self.user = Users(
#         #     Username=self.username.data,
#         #     Email=self.email.data,
#         #     password=bcrypt.generate_password_hash(self.password.data),
#         # )

#         # Redirect to the user's profile page
#         return redirect(self.user.get_profile_url())
    
#     def get_profile_url(self):
#             return f"/profile/{self.Username}"
    
# class RegisterForm(FlaskForm):
#     """Register form."""

#     username = StringField("Username", validators=[DataRequired(), Length(min=3, max=25)])
#     email = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=40)])
#     password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=40)])
#     confirm_password = PasswordField(
#         "Confirm Password",
#         [DataRequired(), EqualTo("password", message="Passwords must match")],
#     )
#     submit = SubmitField("Register")

#     def validate(self, **kwargs):
#         """Validate the form."""
#         if not super().validate(**kwargs):
#             return False
#         user = Users.query.filter_by(Username=self.username.data).first()
#         if user:
#             self.username.errors.append("Username already registered")
#             return False
#         # todo find a smarter method for email validation? or at least one that's compatible with Heroku
#         user = Users.query.filter_by(Email=self.email.data).first()
#         if user:
#             self.email.errors.append("Email already registered")
#             return False
# # findme when the above block is worked out -- remember to clean email-validator==2.1.0.post1 from requirements.txt

#         # Update the user model with hashed password
#         self.user = Users(
#             Username=self.username.data,
#             Email=self.email.data,
#             password=bcrypt.generate_password_hash(self.password.data),
#         )

#         # Redirect to the user's profile page
#         return redirect(self.user.get_profile_url())

#     def __init__(self, *args, **kwargs):
#         """Create instance."""
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.user = None

# class ProfileForm(FlaskForm):
#     fname = StringField("First Name")
#     lname = StringField("Last Name")
#     bio = TextAreaField("Bio")
#     profile_pic = FileField("Profile Picture", validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
#     submit = SubmitField("Save")

# class Search_Farms(FlaskForm):

#     location = StringField('Address',
#                         validators=[DataRequired(), Length(min=5, max=30)],
#                         render_kw={'placeholder': '55555 Sleighbell St. Northpole, NP 00001'}) 
#     submit = SubmitField('Look for Sites')

