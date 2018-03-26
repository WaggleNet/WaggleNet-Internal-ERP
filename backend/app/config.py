from os import environ


class Config(object):
    DEBUG = True if environ.get('DEBUG', False) else False
    TESTING = True if environ.get('TESTING', False) else False
    SECRET_KEY = environ.get('SECRET', 'PXIUHSX?"Y>{I*(#G{DYI;)192KJHC')
    SQLALCHEMY_DATABASE_URI = environ.get('DB', 'postgres+psycopg2://localhost/wagglenet-erp')
    SQLALCHEMY_TRACK_MODIFICATIONS = True