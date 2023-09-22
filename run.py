from app import app
from config import Config

app.secret_key = Config.SECRET_KEY  # Set a secret key for flash messages

if __name__ == '__main__':
    app.run(debug=True)
