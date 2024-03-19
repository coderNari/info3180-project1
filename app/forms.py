from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    rooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathrooms = IntegerField('No of Bathrooms', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'),('Apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    