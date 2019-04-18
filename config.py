import os

DEBUG = bool(os.getenv('DEBUG', 0))
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_URI')
MONGODB_HOST = os.getenv('MONGODB_URI')
SECRET_KEY = os.getenv('SECRET_KEY')
THREADS_PER_PAGE = 2
SQLALCHEMY_TRACK_MODIFICATIONS = False
