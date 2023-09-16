from app import app
from config import Config

app.secret_key = Config.SECRET_KEY  # Set a secret key for flash messages

if __name__ == '__main__':
    app.run(debug=True)
    
# Create a SQLAlchemy database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"