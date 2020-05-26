from datetime import datetime
import string
import random


def convert_date_from_html(html_date_string):
    """Converts dates got from html forms"""
    yy,mm,dd = html_date_string.split("-")
    return datetime(int(yy),int(mm),int(dd))


def randomString(stringLength=12):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))