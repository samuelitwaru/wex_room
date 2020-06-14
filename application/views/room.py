from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Room, db, PricingCategory, Booking
from application.forms.room import RegisterRoomForm, EditRoomForm, DeleteRoomForm, FilterRoomForm


room_bp = Blueprint('room_bp', __name__, url_prefix="/room")


@room_bp.route("/")
def get_rooms():
	filter_form = FilterRoomForm(request.args)
	filter_form.pricing_category_id.choices = [(pricing_category.id, pricing_category.name) for pricing_category in PricingCategory.query.all()]
	
	# get request args
	pricing_category_id = request.args.get('pricing_category_id')	
	query = request.args.get('query') 
	
	# search code
	if query:
		rooms = Room.query.whooshee_search(query).all()

	# filter code
	elif pricing_category_id:
		rooms = Room.query.filter_by(pricing_category_id=pricing_category_id).all()
	
	# if not searching or filtering
	else:
		rooms = Room.query.all()

	return render_template('room/rooms.html', rooms=rooms, filter_form=filter_form)


@room_bp.route("/register", methods=['GET', 'POST'])
def register_room():
	form = RegisterRoomForm()
	form.pricing_category_id.choices = [(pricing_category.id, pricing_category.name) for pricing_category in PricingCategory.query.all()]
	if form.validate_on_submit():
		# get request parameters
		name = request.form.get("name")
		pricing_category_id = request.form.get("pricing_category_id")
		# register room
		room = Room(name=name, pricing_category_id=pricing_category_id)
		db.session.add(room)
		db.session.commit()
		id = room.id
		return redirect(url_for('room_bp.edit_room', id=id))
	return render_template('room/register-room.html', form=form)


@room_bp.route("/<id>/edit", methods=['GET', 'POST'])
def edit_room(id):
	room = Room.query.get(id)
	form = EditRoomForm(obj=room)
	form.pricing_category_id.choices = [(pricing_category.id, pricing_category.name) for pricing_category in PricingCategory.query.all()]
	if form.validate_on_submit():
		# get request parameters
		name = request.form.get("name")
		pricing_category_id = request.form.get("pricing_category_id")
		# edit room
		room.name = name
		room.pricing_category_id = pricing_category_id
		db.session.commit()
		return redirect(url_for('room_bp.edit_room', id=id))
	return render_template('room/edit-room.html', form=form, room=room)


@room_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_room(id):
	room = Room.query.get(id)
	form = DeleteRoomForm(obj=room)
	if form.validate_on_submit():
		db.session.delete(room)
		db.session.commit()
		return redirect(url_for('room_bp.get_rooms'))
	return render_template('room/delete-room.html', form=form, room=room)


# secondary routes
@room_bp.route("/<id>/bookings")
def get_room_bookings(id):
	room = Room.query.get(id)
	bookings = room.bookings
	return render_template('booking/secondary-bookings.html', parent_template='room/room.html', room=room, bookings=bookings)
