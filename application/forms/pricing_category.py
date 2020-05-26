from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea, HiddenInput


class RegisterPricingCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[], widget=TextArea())
    price_per_day = IntegerField('Price per day')
    price_per_week = IntegerField('Price per week')
    price_per_month = IntegerField('Price per month')
    submit = SubmitField('Register')


class EditPricingCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[], widget=TextArea())
    price_per_day = IntegerField('Pricing per day')
    price_per_week = IntegerField('Price per week')
    price_per_month = IntegerField('Price per month')
    submit = SubmitField('Save')


class DeletePricingCategoryForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
    submit = SubmitField('Yes')
