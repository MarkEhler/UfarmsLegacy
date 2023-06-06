import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_PATH = os.path.join(APP_PATH, 'Ufarms/app/templates/')
    STATIC_PATH = os.path.join(APP_PATH, 'Ufarms/app/static/')
    DATA_PATH = os.path.join(APP_PATH, 'Ufarms/app/data/')