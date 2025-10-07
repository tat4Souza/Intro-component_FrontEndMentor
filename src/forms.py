from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email

class FormLogin(FlaskForm):
    first_name = StringField("Name:", validators=[DataRequired("First Name cannot be empty")])
    last_name = StringField("Last Name:", validators=[DataRequired("Last Name cannot be empty")])
    email = StringField("Email Address:", validators=[DataRequired("Email cannot be empty"), Email("Looks like this is not an email")])
    password = PasswordField("Password:", validators=[DataRequired("Password cannot be empty")])
    btn_submit = SubmitField("Claim your free trial")