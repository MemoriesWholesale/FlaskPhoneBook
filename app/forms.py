from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    first_name = StringField('First Name',validators=[InputRequired()])
    last_name = StringField('Last Name',validators=[InputRequired()])
    phone = StringField('Phone',validators=[InputRequired()])
    address = StringField('Address')
    submit = SubmitField('Add Contact')