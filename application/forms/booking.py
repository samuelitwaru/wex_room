from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, ValidationError
import datetime
from application.utilities import convert_date_from_html

# validators
def not_less_today(form, field):
    today = datetime.datetime.utcnow()
    if field.data < datetime.date(today.year, today.month,today.day):
        raise ValidationError(f'Checkin date should start from today ({today.strftime("%d %b %Y")})')


class RegisterBookingForm(FlaskForm):
    customer_id = SelectField('Select Customer', validators=[DataRequired()], coerce=int)
    pricing_period = SelectField('Select Pricing', validators=[DataRequired()], coerce=str)
    period = IntegerField("Time Period", validators=[DataRequired()])
    checkin_date = DateField("Checkin Date", validators=[DataRequired(), not_less_today])
    submit = SubmitField('Book')


class EditBookingForm(FlaskForm):
    customer_id = SelectField('Select Customer', validators=[DataRequired()], coerce=int)
    pricing_period = SelectField('Select Pricing', validators=[DataRequired()], coerce=str)
    period = IntegerField("Time Period", validators=[DataRequired()])
    checkin_date = DateField("Checkin Date", validators=[DataRequired(), not_less_today])
    submit = SubmitField('Save')


class DeleteBookingForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')


class FilterBookingForm(FlaskForm):
    book_date_gte = DateField("Book Date (lower)")
    book_date_lte = DateField("Book Date (upper)")
    checkin_date_gte = DateField("Checkin Date (lower)")
    checkin_date_lte = DateField("Checkin Date (upper)")
    customer_id = SelectField("Customer")
    room_id = SelectField("Room")
    submit = SubmitField('Filter')


# Other Forms
class SelectRoomForm(FlaskForm):
    room_id = SelectField('Select Room', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Next')