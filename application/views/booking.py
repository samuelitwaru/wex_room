from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Booking, db, Room, Customer
from application.forms.booking import RegisterBookingForm, EditBookingForm, DeleteBookingForm, FilterBookingForm, SelectRoomForm
from datetime import datetime
from application.utilities import convert_date_from_html, get_pricing_choices
from application.guards.data import allow_unbooked_room
from application.filters.model_filters import filter_booking

booking_bp = Blueprint('booking_bp', __name__, url_prefix="/booking")


@booking_bp.route("/", methods=["POST", "GET"])
def get_bookings():
	filter_form = FilterBookingForm(request.args)
	filter_form.customer_id.choices = [("", "All")]+[(customer.id, customer.full_name) for customer in Customer.query.all()]
	filter_form.room_id.choices = [("", "All")]+[(room.id, room.name) for room in Room.query.all()]

	# get request args
	book_date_gte = request.args.get('book_date_gte')	
	book_date_lte = request.args.get('book_date_lte')
	checkin_date_gte = request.args.get('checkin_date_gte')	
	checkin_date_lte = request.args.get('checkin_date_lte')	
	customer_id = request.args.get('customer_id')	
	room_id = request.args.get('room_id')

	# if filtering: filter code
	if book_date_gte or book_date_lte or checkin_date_gte or checkin_date_lte or customer_id or room_id:
		bookings = filter_booking(book_date_gte=book_date_gte, book_date_lte=book_date_lte,
			checkin_date_gte=checkin_date_gte, checkin_date_lte=checkin_date_lte,
			customer_id=customer_id, room_id=room_id
			)
	# if not filtering
	else:
		bookings = Booking.query.all()
	
	form = SelectRoomForm()
	form.room_id.choices = [(room.id, room.name) for room in Room.query.all()]
	if form.validate_on_submit():
		return redirect(url_for('booking_bp.register_booking', room_id=request.form.get("room_id")))

	return render_template('booking/bookings.html', bookings=bookings, form=form, filter_form=filter_form)


@booking_bp.route("/register/<room_id>", methods=['GET', 'POST'])
@allow_unbooked_room
def register_booking(room_id):
	room = Room.query.get(room_id)
	form = RegisterBookingForm()
	form.customer_id.choices = [(customer.id, customer.full_name) for customer in Customer.query.all()]
	form.pricing_period.choices = get_pricing_choices(room)

	if form.validate_on_submit():
		# get request parameters
		customer_id = request.form.get("customer_id")
		pricing_period = request.form.get("pricing_period")
		period = request.form.get("period")
		checkin_date = request.form.get("checkin_date")
		# register booking
		if pricing_period == "day": price_per_period=room.pricing_category.price_per_day; pricing_period="day"
		elif pricing_period == "week": price_per_period=room.pricing_category.price_per_week; pricing_period="week"
		elif pricing_period == "month": price_per_period=room.pricing_category.price_per_month; pricing_period="month"
		booking = Booking(customer_id=customer_id, room_id=room.id, pricing_period=pricing_period, period=period, price_per_period=price_per_period, book_date=datetime.utcnow(), checkin_date=convert_date_from_html(checkin_date))
		db.session.add(booking)
		db.session.commit()
		return redirect(url_for('room_bp.edit_room', id=room.id))
	
	return render_template('booking/register-booking.html', form=form, room=room)


@booking_bp.route("/<id>/edit", methods=['GET', 'POST'])
def edit_booking(id):
	booking = Booking.query.get(id)
	room = booking.room
	form = EditBookingForm(obj=booking)
	form.customer_id.choices = [(customer.id, customer.full_name) for customer in Customer.query.all()]
	form.pricing_period.choices = get_pricing_choices(room)

	if form.validate_on_submit():
		# get request parameters
		customer_id = request.form.get("customer_id")
		pricing_period = request.form.get("pricing_period")
		period = request.form.get("period")
		checkin_date = request.form.get("checkin_date")
		
		# edit booking
		if pricing_period == "day": price_per_period=room.pricing_category.price_per_day; pricing_period="day"
		elif pricing_period == "week": price_per_period=room.pricing_category.price_per_week; pricing_period="week"
		elif pricing_period == "month": price_per_period=room.pricing_category.price_per_month; pricing_period="month"
		booking.customer_id = customer_id
		booking.pricing_period = pricing_period
		booking.price_per_period = price_per_period
		booking.period = period
		booking.checkin_date = convert_date_from_html(checkin_date)
		db.session.commit()
		return redirect(url_for('booking_bp.edit_booking', id=id))
	return render_template('booking/edit-booking.html', form=form, booking=booking, room=room)


@booking_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_booking(id):
	booking = Booking.query.get(id)
	form = DeleteBookingForm(obj=booking)
	if form.validate_on_submit():
		db.session.delete(booking)
		db.session.commit()
		return redirect(url_for('booking_bp.get_bookings'))
	return render_template('booking/delete-booking.html', form=form, booking=booking)
