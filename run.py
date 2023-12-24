from app import app
from config import Config

app.secret_key = Config.SECRET_KEY  # Set a secret key for flash messages

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
