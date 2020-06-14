from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Payment, db, Booking
from application.forms.payment import RegisterPaymentForm, EditPaymentForm, DeletePaymentForm
from datetime import datetime

payment_bp = Blueprint('payment_bp', __name__, url_prefix="/payment")


@payment_bp.route("/")
def get_payments():
	bookings = Booking.query.all()
	return render_template('payment/payments.html', bookings=bookings)


@payment_bp.route("/register/<booking_id>", methods=['GET', 'POST'])
def register_payment(booking_id):
	booking = Booking.query.get(booking_id)
	form = RegisterPaymentForm()
	form.booking_id.data = booking_id
	if form.validate_on_submit():
		# get request parameters
		amount = request.form.get("amount")
		
		# register payment
		payment = Payment(amount=amount, date=datetime.utcnow(), booking_id=booking_id)
		db.session.add(payment)
		db.session.commit()
		id = payment.id
		return redirect(url_for('payment_bp.register_payment', booking_id=booking_id))
	return render_template('payment/register-payment.html', form=form, booking=booking)


@payment_bp.route("/<id>/edit", methods=['GET', 'POST'])
def edit_payment(id):
	payment = Payment.query.get(id)
	booking = payment.booking
	form = EditPaymentForm(obj=payment)
	if form.validate_on_submit():
		# get request parameters
		amount = request.form.get("amount")
		
		# edit payment
		payment.amount = amount
		db.session.commit()
		return redirect(url_for('payment_bp.edit_payment', id=id))
	return render_template('payment/edit-payment.html', form=form, payment=payment, booking=booking)


@payment_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_payment(id):
	payment = Payment.query.get(id)
	booking = payment.booking
	form = DeletePaymentForm(obj=payment)
	if form.validate_on_submit():
		db.session.delete(payment)
		db.session.commit()
		return redirect(url_for('payment_bp.get_payments'))
	return render_template('payment/delete-payment.html', form=form, payment=payment, booking=booking)


