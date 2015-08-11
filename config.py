import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres@localhost/workingregister')
    CURRENT_REGISTER_API = os.getenv('CURRENT_REGISTER_API', 'http://localhost:5007')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class UnitTestConfig(Config):
    #Class needed so no messages not actually published by tests.
    DEBUG = True

class TestConfig(Config):
    DEBUG = True

class PreproductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
