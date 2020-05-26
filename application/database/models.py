from application import db
from datetime import datetime, timedelta

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    pricing_category_id = db.Column(db.Integer, db.ForeignKey("pricing_category.id"))
    bookings = db.relationship("Booking", backref="room")

    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String())
    email = db.Column(db.String())
    telephone = db.Column(db.String())
    date_registered = db.Column(db.DateTime())
    bookings = db.relationship("Booking", backref="customer")

    
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_number = db.Column(db.String())
    book_date = db.Column(db.DateTime())
    checkin_date = db.Column(db.DateTime())
    checkout_date = db.Column(db.DateTime())
    period = db.Column(db.Integer())
    pricing_period = db.Column(db.String())
    price_per_period = db.Column(db.Integer())
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    payments = db.relationship("Payment", backref="booking")

    def total_paid(self):
        return sum([payment.amount for payment in self.payments])

    def checkout_date(self):
        if self.pricing_period == "day": period = self.period 
        elif self.pricing_period == "week": period = self.period*7 
        elif self.pricing_period == "month": period = self.period*30
        return self.checkin_date+timedelta(period)

    
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    amount = db.Column(db.Integer())
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.id"))

    
class PricingCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    price_per_day = db.Column(db.Integer())
    price_per_week = db.Column(db.Integer())
    price_per_month = db.Column(db.Integer())
    rooms = db.relationship("Room", backref="pricing_category")
