from application.utilities import convert_date_from_html
from application.database.models import Booking

def filter_booking(**kwargs):
	book_date_gte = kwargs.get('book_date_gte')   
	book_date_lte = kwargs.get('book_date_lte')
	checkin_date_gte = kwargs.get('checkin_date_gte') 
	checkin_date_lte = kwargs.get('checkin_date_lte') 
	customer_id = kwargs.get('customer_id')   
	room_id = kwargs.get('room_id')

	query = Booking.query
	if book_date_gte:
	    query = query.filter(Booking.book_date>=convert_date_from_html(book_date_gte, date_time=False))
	if book_date_lte:
	    query = query.filter(Booking.book_date<=convert_date_from_html(book_date_lte, date_time=False))
	if checkin_date_gte:
	    query = query.filter(Booking.checkin_date>=convert_date_from_html(checkin_date_gte))
	if checkin_date_lte:
	    query = query.filter(Booking.checkin_date<=convert_date_from_html(checkin_date_lte))
	if customer_id:
	    query = query.filter(Booking.customer_id==customer_id)
	if room_id:
	    query = query.filter(Booking.room_id==room_id)

	return query.all()