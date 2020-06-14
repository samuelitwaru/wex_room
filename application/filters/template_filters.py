from application import app


@app.template_filter()
def comma_separator(value):
    if isinstance(value, int):
    	return f'{value:,}'
    return value


@app.template_filter(name="format_date")
def format_date(date):
	if date:
		date = date.strftime("%d %b %Y")
		return date
	return date
