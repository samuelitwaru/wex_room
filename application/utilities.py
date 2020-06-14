from datetime import datetime, date
import string
import random


def convert_date_from_html(html_date_string, date_time=True):
    """Converts dates got from html forms"""
    yy,mm,dd = html_date_string.split("-")
    if date_time:
    	return datetime(int(yy),int(mm),int(dd))
    return date(int(yy),int(mm),int(dd))


def randomString(stringLength=12):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def get_pricing_choices(room):
	"""generate a list of pricing choices available for a room"""
	pricing_choices = []
	if room.pricing_category.price_per_day:
		pricing_choices.append(("day", f"{room.pricing_category.price_per_day} per day"))
	if room.pricing_category.price_per_week:
		pricing_choices.append(("week", f"{room.pricing_category.price_per_week} per week"))
	if room.pricing_category.price_per_month:
		pricing_choices.append(("month", f"{room.pricing_category.price_per_month} per month"))
	return pricing_choices
