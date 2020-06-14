from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import HiddenInput
from application.database.models import Room

# validators
def unique_create_name(form, field):
    if Room.query.filter_by(name=field.data).first():
        raise ValidationError(f"Room '{field.data}' already exists.")


def unique_update_name(form, field):
    pass
    # EditRoomForm should be adjusted first

class RegisterRoomForm(FlaskForm):
    name = StringField('Room Name/Number', validators=[DataRequired(), unique_create_name])
    pricing_category_id = SelectField('Pricing Category', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Register')


class EditRoomForm(FlaskForm):
    name = StringField('Room Name/Number', validators=[DataRequired()])
    pricing_category_id = SelectField('Pricing Category', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Save')


class DeleteRoomForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()], widget=HiddenInput())
    submit = SubmitField('Yes')


class FilterRoomForm(FlaskForm):
    pricing_category_id = SelectField("Select Pricing Category", coerce=int)
    submit = SubmitField('Filter')
