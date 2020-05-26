from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email


class RegisterCustomerForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    telephone = StringField('Telephone Number', validators=[])
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Register')


class EditCustomerForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    telephone = StringField('Telephone Number')
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Save')


class DeleteCustomerForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')


'''
telephone validation
- use regex (custom)
delete_Customer
- pass in the customer id from route and ensure that its the same from the field
'''



    
