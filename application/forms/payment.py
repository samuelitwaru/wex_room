from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from application.database.models import Booking

# validators
def amount_between_0_and_balance(form, field):
	booking = Booking.query.get(form.booking_id.data)
	balance = booking.balance()
	if not(0 < field.data <= balance): 
		raise ValidationError(f"Invalid amount entered. Should be from 0 - {balance:,}")

class RegisterPaymentForm(FlaskForm):
    booking_id = IntegerField()
    amount = IntegerField('Enter Amount', validators=[DataRequired(), amount_between_0_and_balance])
    submit = SubmitField('Make Payment')


class EditPaymentForm(FlaskForm):
    booking_id = IntegerField()
    amount = IntegerField('Change Amount', validators=[DataRequired()])
    submit = SubmitField('Save')


class DeletePaymentForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')
