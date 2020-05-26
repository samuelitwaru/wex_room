from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import HiddenInput
from application.database.models import PricingCategory, db


class RegisterRoomForm(FlaskForm):
    name = StringField('Room Name/Number', validators=[DataRequired()])
    pricing_category = SelectField('Pricing Category', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Register')


class EditRoomForm(FlaskForm):
    name = StringField('Room Name/Number', validators=[DataRequired()])
    pricing_category = SelectField('Pricing Category', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Save')


class DeleteRoomForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
    submit = SubmitField('Yes')
