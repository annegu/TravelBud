from flask.json.tag import PassDict
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.core import DecimalField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.widgets.core import Select

# TODOS
# phone number validation figure out how to dynamically accept dropdown options


#Signup Form
class SignUpForm(FlaskForm):
    full_name = StringField('Full Name', validators = [InputRequired()])
    email = StringField('Email',
                        validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators = [InputRequired(), EqualTo('password')])
    age = IntegerField("Age")
    submit = SubmitField('Sign Up')

class addNewCourse(FlaskForm):
    courseCode = StringField('Course Code', validators = [InputRequired()])
    numLabs = StringField('How many labs are there?',validators = [InputRequired()])
    numPS = StringField('How many sets are there?', validators = [InputRequired()])
    numLectures = StringField('How many lectures are there?', validators = [InputRequired()])
    submit = SubmitField('Add Course')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    
    submit = SubmitField('Login')

# NEW CHANGE
class phoneAuthenticationForm(FlaskForm):
    countryCode = SelectField('Country Code', choices=[('1-United States'), ('1-Canada')])
    phoneNumber = IntegerField('Your Phone Number', validators = [InputRequired()])
    submit = SubmitField('Send Code')

# NEW CHANGE
class verify(FlaskForm):
    verificationCode = IntegerField('Verfication Code')
    submit = SubmitField('Verify')

class findCourse(FlaskForm):
    courseCode = StringField('Course Code', validators = [InputRequired()])
    submit = SubmitField('Find Course')