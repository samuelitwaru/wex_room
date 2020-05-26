from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Email


class RegisterBookingForm(FlaskForm):
    customer_id = SelectField('Select Customer', validators=[DataRequired()], coerce=int)
    pricing_period = SelectField('Select Pricing', validators=[DataRequired()], coerce=str)
    period = IntegerField("Time Period", validators=[DataRequired()])
    checkin_date = DateField("Checkin Date", validators=[DataRequired()])
    submit = SubmitField('Book')


class EditBookingForm(FlaskForm):
    customer_id = SelectField('Select Customer', validators=[DataRequired()], coerce=int)
    pricing_period = SelectField('Select Pricing', validators=[DataRequired()], coerce=str)
    period = IntegerField("Time Period", validators=[DataRequired()])
    checkin_date = DateField("Checkin Date", validators=[DataRequired()])
    submit = SubmitField('Save')


class DeleteBookingForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')


# Other Forms
class SelectRoomForm(FlaskForm):
    room_id = SelectField('Select Room', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Next')