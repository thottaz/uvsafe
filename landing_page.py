from flask import (
    Blueprint, request, redirect, url_for, flash, g, render_template
)

landing_page_bp = Blueprint('landing_page', __name__)

@landing_page_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        # Handle the form submission
        postcode = request.form.get('postcode', '').strip()
        # Do something with the postcode
        # ...
        if not postcode:
            # Handle the error - postcode is required
            flash("Error: postcode is required.")
            return redirect(url_for('landing_page.index'))

        # Redirect to the advice page, passing the postcode as a query parameter
        return redirect(url_for('advice.index', postcode=postcode))

    return render_template('landing_page/index.html')
