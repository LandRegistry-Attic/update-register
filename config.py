import os

class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    # format is dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/workingregister'
    DEBUG = True

class UnitTestConfig(Config):
    #Class needed so no messages not actually published by tests.
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')
    DEBUG = True

class PreproductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
