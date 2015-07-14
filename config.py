import os

class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    # format is dialect+driver://username:password@host:port/database
    CURRENT_REGISTER_API = "http://localhost:5007"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/workingregister'
    DEBUG = True

class UnitTestConfig(Config):
    #Class needed so no messages not actually published by tests.
    CURRENT_REGISTER_API = "http://localhost:5007"
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True

class TestConfig(Config):
    CURRENT_REGISTER_API = "http://localhost:5007"
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')
    DEBUG = True

class PreproductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
