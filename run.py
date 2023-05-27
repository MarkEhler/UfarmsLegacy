from app import app

if __name__ == '__main__':
    app.run(debug=True)
app.secret_key = 'you-will-never-guess'  # Set a secret key for flash messages
