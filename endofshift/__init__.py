from flask import Flask
app = Flask(__name__)

from endofshift.core.views import core
from endofshift.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)

