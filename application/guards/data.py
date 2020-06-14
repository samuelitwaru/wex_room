from functools import wraps
from flask import redirect, url_for
from application.database.models import Room


def allow_unbooked_room(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		room = Room.query.get(kwargs.get("room_id"))
		# if room is NOT FREE
		res = func(*args, **kwargs)
		if room.status() != "FREE":
			return redirect(url_for("room_bp.edit_room", id=room.id))
		# if room is FREE
		return func(*args, **kwargs)
	return wrapper
