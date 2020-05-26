from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email


class RegisterPaymentForm(FlaskForm):
    amount = IntegerField('Enter Amount', validators=[DataRequired()])
    submit = SubmitField('Make Payment')


class EditPaymentForm(FlaskForm):
    amount = IntegerField('Change Amount', validators=[DataRequired()])
    submit = SubmitField('Save')


class DeletePaymentForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Yes')
