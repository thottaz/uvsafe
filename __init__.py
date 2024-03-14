from flask import Flask
from .landing_page import landing_page_bp
from .advice import advice_bp

app = Flask(__name__)
app.register_blueprint(landing_page_bp)
app.register_blueprint(advice_bp)

def create_app(test_config=None):
    # Add your app configuration here
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(landing_page_bp)
    app.register_blueprint(advice_bp)
    return app