import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    # # ...
    # env_var = os.getenv("host")
    # print(f"Value of 'host' environment variable: {env_var}")
    # DB_HOST = env_var.strip() if env_var else "default_host"

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# findme todo ^^^
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_PATH = os.path.join(APP_PATH, 'Ufarms/app/templates/')
    STATIC_PATH = os.path.join(APP_PATH, 'Ufarms/app/static/')
    DATA_PATH = os.path.join(APP_PATH, 'Ufarms/app/data/')

    ENVIRONMENT = os.getenv("ENVIRONMENT")
    if ENVIRONMENT == 'develop':
        DB_HOST = os.getenv("DEV_HOST").strip()
        DB_USER = os.getenv("DEV_USERNAME").strip()
        DB_PASSWORD = os.getenv("DEV_PASSWORD").strip()
        DB_NAME = os.getenv("DEV_DATABASE").strip()
    else:
        DB_HOST = os.getenv("PROD_HOST").strip()
        DB_USER = os.getenv("PROD_USERNAME").strip()
        DB_PASSWORD = os.getenv("PROD_PASSWORD").strip()
        DB_NAME = os.getenv("PROD_DATABASE").strip()