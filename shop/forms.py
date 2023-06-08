from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddUserForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SearchForm(FlaskForm):
    company = StringField('Company')
    product = StringField('Product')
    typename = StringField('TypeName')
    inches = StringField('Inches')
    resolution = StringField('Resolution')
    cpu = StringField('CPU')
    ram = StringField('RAM (GB)')
    memory = StringField('Memory')
    gpu = StringField('GPU')
    opsys = StringField('Operating System')
    weight = StringField('Weight')
    price_euros = StringField('Price (Euros)')
    submit = SubmitField('Search')

class SellForm(FlaskForm):
    company = StringField('Company')
    product = StringField('Product')
    typename = StringField('TypeName')
    inches = DecimalField('Inches')
    resolution = StringField('Resolution')
    cpu = StringField('CPU')
    ram = DecimalField('RAM (GB)')
    memory = StringField('Memory')
    gpu = StringField('GPU')
    opsys = StringField('Operating System')
    weight = DecimalField('Weight')
    price_euros = DecimalField('Price (Euros)')
    submit = SubmitField('Sell')