# from flask import Flask
# from config import Config
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_cors import CORS

# # findme does this replace need for explicit mentions?
# app = Flask(__name__) #, static_folder='static', template_folder='templates')
# app.config.from_object(Config)
# app.secret_key = Config.SECRET_KEY

# # Create a SQLAlchemy database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f"mysql+mysqlconnector://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"
#     f"?ssl_ca={Config.APP_PATH}/isrgrootx1.pem"
# )
# # findme consider hiding .pem file
    
# db = SQLAlchemy(app)
# bootstrap = Bootstrap(app)
# migrate = Migrate(app, db)
# bcrypt = Bcrypt()
# CORS(app)
# from app import routes, models

