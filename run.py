from app import app
import settings

if __name__ == '__main__':
    app.run(debug=True)
    
app.secret_key = 'you-will-never-guess'  # Set a secret key for flash messages
