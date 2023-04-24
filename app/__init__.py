from flask import Flask # send_from_directory
from config import Config
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
app.secret_key = os.urandom(24)

from app import routes, errors