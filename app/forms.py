from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField #the type of input
from wtforms.validators import InputRequired, DataRequired , Length #The wtf form has validators
from flask_wtf.file import FileField, FileRequired, FileAllowed  #

class PropertyForm(FlaskForm):
     title = StringField('Title', validators=[InputRequired()])
     bednum = IntegerField('Bedrooms', validators=[InputRequired()])
     bathnum= IntegerField('Bathrooms', validators=[InputRequired()])
     location= StringField('Location', validators=[InputRequired()])
     price=IntegerField('Price', validators=[InputRequired()])
     proptype=SelectField("Type", choices=["Apartment","House"])
     descr=TextAreaField("Description",validators=[DataRequired(),InputRequired(),Length(max=700)])
     photo=FileField("Photo", validators=[FileRequired(),FileAllowed(["jpg", "png","jpeg","Images only!"])])
     