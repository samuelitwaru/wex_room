from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import Customer, db
from application.forms.customer import RegisterCustomerForm, EditCustomerForm, DeleteCustomerForm


customer_bp = Blueprint('customer_bp', __name__, url_prefix="/customer")


@customer_bp.route("/")
def get_customers():
	query = request.args.get('query') 
	if query:
		customers = Customer.query.whooshee_search(query).all()
	else:
		customers = Customer.query.all()
	return render_template('customer/customers.html', customers=customers)


@customer_bp.route("/register", methods=['GET', 'POST'])
def register_customer():
	form = RegisterCustomerForm()
	if form.validate_on_submit():
		# get request parameters
		full_name = request.form.get("full_name")
		telephone = request.form.get("telephone")
		email = request.form.get("email")
		
		# register customer
		customer = Customer(full_name=full_name, telephone=telephone, email=email)
		db.session.add(customer)
		db.session.commit()
		id = customer.id
		return redirect(url_for('customer_bp.edit_customer', id=id))
	return render_template('customer/register-customer.html', form=form)


@customer_bp.route("/<id>/edit", methods=['GET', 'POST'])
def edit_customer(id):
	customer = Customer.query.get(id)
	form = EditCustomerForm(obj=customer)
	if form.validate_on_submit():
		# get request parameters
		full_name = request.form.get("full_name")
		telephone = request.form.get("telephone")
		email = request.form.get("email")
		
		# edit customer
		customer.full_name = full_name
		customer.telephone = telephone
		customer.email = email
		db.session.commit()
		return redirect(url_for('customer_bp.edit_customer', id=id))
	return render_template('customer/edit-customer.html', form=form, customer=customer)


@customer_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_customer(id):
	customer = Customer.query.get(id)
	form = DeleteCustomerForm(obj=customer)
	if form.validate_on_submit():
		db.session.delete(customer)
		db.session.commit()
		return redirect(url_for('customer_bp.get_customers'))
	return render_template('customer/delete-customer.html', form=form, customer=customer)


# secondary routes
@customer_bp.route("/<id>/bookings")
def get_customer_bookings(id):
	customer = Customer.query.get(id)
	bookings = customer.bookings
	return render_template('booking/secondary-bookings.html', parent_template='customer/customer.html', customer=customer, bookings=bookings)
