from app import app

if __name__ == '__main__':
    app.run(debug=True)
    
app.secret_key = SECRET_KEY  # Set a secret key for flash messages
