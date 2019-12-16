# /src/config.py

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    #JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'

    #SQLALCHEMY_DATABASE_URI = os.getenv('postgresql+psycopg2://postgres:password@localhost:5432/blog_api_db')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://postgres:password@localhost:5432/blog_api_db'

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    #SQLALCHEMY_DATABASE_URI = os.getenv('postgresql+psycopg2://postgres:password@localhost:5432/blog_api_db')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://postgres:password@localhost:5432/blog_api_db'


    print("database string value") #******************CHECK************************
    print(SQLALCHEMY_DATABASE_URI )
    print("database URL")
    #print(DATABASE_URL)


    #JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    # Hardcoded JWT_SECRET_KEY for Windows users
    JWT_SECRET_KEY = os.getenv('hhgaghhgsdhdhdd')


class Testing(object):
    """
    Development environment configuration
    """
    TESTING = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('postgresql+psycopg2://postgres:password@localhost:5432/blog_api_db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
    #print("Enviromment Name:")
    #print(env_name)

