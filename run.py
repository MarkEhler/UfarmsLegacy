import time
from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# , static_folder='ufarms-react-client/build', static_url_path=''
CORS(app)

@app.route('/time')
@cross_origin()
def get_current_time():
    return {'time': time.time()}

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()