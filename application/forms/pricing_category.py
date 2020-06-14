from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets import TextArea, HiddenInput
from application.database.models import PricingCategory


# validators
def unique_create_name(form, field):
    if PricingCategory.query.filter_by(name=field.data).first():
        raise ValidationError(f"Pricing Category '{field.data}' already exists.")

def integer_type(form, field):
    if field.data:
        try:
            int(field.data)
        except:
            raise ValidationError('Field must be an integer')


def pricing_required(form, field):
    if not (field.data or form.price_per_week.data or form.price_per_month.data):
        form.errors['pricing'] = []
        form.errors['pricing'].append('At least one price should be set')
        raise ValidationError()


# forms
class RegisterPricingCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), unique_create_name])
    description = StringField('Description', validators=[], widget=TextArea())
    price_per_day = StringField('Price per day', validators=[pricing_required, integer_type])
    price_per_week = StringField('Price per week', validators=[integer_type])
    price_per_month = StringField('Price per month', validators=[integer_type])
    submit = SubmitField('Register')


class EditPricingCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[], widget=TextArea())
    price_per_day = StringField('Price per day', validators=[pricing_required, integer_type])
    price_per_week = StringField('Price per week', validators=[integer_type])
    price_per_month = StringField('Price per month', validators=[integer_type])
    submit = SubmitField('Save')


class DeletePricingCategoryForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
    submit = SubmitField('Yes')