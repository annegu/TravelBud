from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class SignUpForm(FlaskForm):
    full_name = StringField('Full Name', validators = [InputRequired()])
    email = StringField('Email',
                        validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class addNewCourse(FlaskForm):
    courseCode = StringField('Course Code', validators = [InputRequired()])
    numLabs = StringField('How many labs are there?',validators = [InputRequired()])
    numPS = StringField('How many sets are there?', validators = [InputRequired()])
    numLectures = StringField('How many lectures are there?', validators = [InputRequired()])
    submit = SubmitField('Add Course')