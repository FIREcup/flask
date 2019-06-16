import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hard to guess string')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[ FLASKY]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://yangtao:123@192.168.31.12/flask"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://yangtao:123@192.168.31.12/flask"


class ProductionConfig(Config):
    PRODUCTION = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql:L//yangtao:123@192.168.31.12/flask"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
