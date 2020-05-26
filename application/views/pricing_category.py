from flask import Blueprint, request, render_template, redirect, url_for
from application.database.models import PricingCategory, db
from application.forms.customer import RegisterCustomerForm, EditCustomerForm, DeleteCustomerForm
from application.forms.pricing_category import RegisterPricingCategoryForm, EditPricingCategoryForm, DeletePricingCategoryForm


pricing_category_bp = Blueprint('pricing_category_bp', __name__, url_prefix="/pricing-category")


@pricing_category_bp.route("/")
def get_pricing_categories():
	pricing_categories = PricingCategory.query.all()
	return render_template('pricing_category/pricing-categories.html', pricing_categories=pricing_categories)


@pricing_category_bp.route("/register", methods=['GET', 'POST'])
def register_pricing_category():
	form = RegisterPricingCategoryForm()
	if form.validate_on_submit():
		# get request parameters
		name = request.form.get("name")
		description = request.form.get("description")
		price_per_day = request.form.get("price_per_day")
		price_per_week = request.form.get("price_per_week")
		price_per_month = request.form.get("price_per_month")
		
		# register pricing_category
		pricing_category = PricingCategory(name=name, description=description, price_per_day=price_per_day, price_per_week=price_per_week, price_per_month=price_per_month)
		db.session.add(pricing_category)
		db.session.commit()
		id = pricing_category.id
		return redirect(url_for('pricing_category_bp.edit_pricing_category', id=id))
	return render_template('pricing_category/register-pricing-category.html', form=form)


@pricing_category_bp.route("/<id>/edit", methods=['GET', 'POST'])
def edit_pricing_category(id):
	pricing_category = PricingCategory.query.get(id)
	form = EditPricingCategoryForm(obj=pricing_category)
	if form.validate_on_submit():
		# get request parameters
		name = request.form.get("name")
		description = request.form.get("description")
		price_per_day = request.form.get("price_per_day")
		price_per_week = request.form.get("price_per_week")
		price_per_month = request.form.get("price_per_month")
		
		# edit pricing_category
		pricing_category.name = name
		pricing_category.description = description
		pricing_category.price_per_day = price_per_day
		pricing_category.price_per_week = price_per_week
		pricing_category.price_per_month = price_per_month
		db.session.commit()
		return redirect(url_for('pricing_category_bp.edit_pricing_category', id=id))
	return render_template('pricing_category/edit-pricing-category.html', pricing_category=pricing_category, form=form)


@pricing_category_bp.route("/<id>/delete", methods=['GET', 'POST'])
def delete_pricing_category(id):
	pricing_category = PricingCategory.query.get(id)
	form = DeletePricingCategoryForm(obj=pricing_category)
	if form.validate_on_submit():
		db.session.delete(pricing_category)
		db.session.commit()
		return redirect(url_for('pricing_category_bp.get_pricing_categories'))
	return render_template('pricing_category/delete-pricing-category.html', form=form, pricing_category=pricing_category)

