from flask import (
    Blueprint, request, redirect, url_for, flash, g, render_template
)
from .functions import get_advice

advice_bp = Blueprint('advice', __name__)

@advice_bp.route('/advice', endpoint='index')
def index():
    # Retrieve the postcode from the query parameter
    postcode = request.args.get('postcode', '')

    # Process the postcode (e.g., find advice specific to that postcode)
    advice = get_advice(postcode)
    # Render the advice page, passing any necessary data
    #return render_template('advice/index.html', postcode=postcode)
    return render_template('advice/index.html', postcode=postcode, advice=advice)

