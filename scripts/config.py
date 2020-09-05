import os

DATABASE_NAME="database.db"

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite://%s'%DATABASE_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig