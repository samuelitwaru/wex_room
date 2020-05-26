from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Room, db, PricingCategory
from application.forms.room import RegisterRoomForm, EditRoomForm, DeleteRoomForm


room_bp = Blueprint('room_bp', __name__, url_prefix="/room")


@room_bp.route("/")
def get_rooms():
	rooms = Room.query.all()
	return render_template('room/rooms.html', rooms=rooms)


@room_bp.route("/register", methods=['GET', 'POST'])
def register_room():
	form = RegisterRoomForm()
	form.pricing_category.choices = [(pricing_category.id, pricing_category.name) for pricing_category in PricingCategory.query.all()]
	if form.validate_on_submit():
		# get request parameters
		name = request.form.get("name")
		pricing_category_id = request.form.get("pricing_category")
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
	form.pricing_category.choices = [(pricing_category.id, pricing_category.name) for pricing_category in PricingCategory.query.all()]
	if form.validate_on_submit():
		# get request parameters
		name = request.form.get("name")
		pricing_category_id = request.form.get("pricing_category")
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
