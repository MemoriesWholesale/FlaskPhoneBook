from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import InputRequired,EqualTo

class ContactForm(FlaskForm):
    first_name = StringField('First Name',validators=[InputRequired()])
    last_name = StringField('Last Name',validators=[InputRequired()])
    phone = StringField('Phone',validators=[InputRequired()])
    email = EmailField('Email')
    address = StringField('Address')
    submit = SubmitField('Add Contact')

class SignupForm(FlaskForm):
    first_name = StringField('First Name*',validators=[InputRequired()])
    last_name = StringField('Last Name*',validators=[InputRequired()])
    username = StringField('Username*',validators=[InputRequired()])
    password = PasswordField('Password*',validators=[InputRequired()])
    confirmpassword = PasswordField('Confirm Password*',validators=[InputRequired(),EqualTo(password,'Passwords do not match! Please try again.')])
    phone = StringField('Phone*',validators=[InputRequired()])
    address = StringField('Address')
    email = EmailField('Email')
    submit = SubmitField('Sign Up!')
    
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    submit = SubmitField('Log In')

class EditForm(FlaskForm):
    pass