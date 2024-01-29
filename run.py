import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

### note ###
# we will create all routes here until further notice


# ## If things are going to be like this I might shift the stack to FastAPI newer -- it's a Flask killer
# Fast example of the above route using Fast

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def get_current_time():
#     return {'time': time.time()}


# ---
# # A draw back of flask is that it requires these sneaky circular-prone imports -- in my experience 90% of the time this is what's causing the error, including the one today -- I think I recall a method for addressing that 
# from app import app
# from config import Config

# app.secret_key = Config.SECRET_KEY  # Set a secret key for flash messages

# # if __name__ == '__main__':
# #     app.run(debug=True)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
