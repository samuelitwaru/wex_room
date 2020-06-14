from flask import Flask
from application import configuration
from flask_sqlalchemy import SQLAlchemy
# import flask_whooshalchemy as whooshalchemy
from flask_whooshee import Whooshee

app = Flask(__name__)

app.config.from_object(configuration.DevelopmentConfig)

db = SQLAlchemy(app)
whooshee = Whooshee(app)

from application.filters.template_filters import *


from application.views.main import main_bp
from application.views.room import room_bp
from application.views.pricing_category import pricing_category_bp
from application.views.booking import booking_bp
from application.views.payment import payment_bp
from application.views.customer import customer_bp

app.register_blueprint(main_bp)
app.register_blueprint(room_bp)
app.register_blueprint(pricing_category_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(customer_bp)
