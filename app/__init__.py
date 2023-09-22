from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

# Create a SQLAlchemy database connection     f"?ssl_ca={Config.APP_PATH}/ca-certificates.crt"
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"

)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)

from app import routes, models


