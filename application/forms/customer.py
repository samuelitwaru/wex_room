from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from application.database.models import Customer

# validators
def unique_create_email(form, field):
    if Customer.query.filter_by(email=field.data).first():
        raise ValidationError(f"The email '{field.data}' already exists.")

def unique_create_telephone(form, field):
    if Customer.query.filter_by(telephone=field.data).first():
        raise ValidationError(f"The telephone number '{field.data}' already exists.")

def unique_update_email(form, field):
    pass
    # EditCustomerForm should be adjusted first

def unique_update_telephone(form, field):
    pass
    # EditCustomerForm should be adjusted first


class RegisterCustomerForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    telephone = StringField('Telephone Number', validators=[unique_create_telephone])
    email = StringField('Email', validators=[Email(), unique_create_email])
    submit = SubmitField('Register')


class EditCustomerForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    telephone = StringField('Telephone Number', validators=[])
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



    
