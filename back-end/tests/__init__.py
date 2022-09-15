from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:q1w2e3r4@127.0.0.1:3306/test?charset=utf8'
