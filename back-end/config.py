import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

class Config(object):
    DEBUG = True

    DIALCT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'q1w2e3r4'
    HOST = '127.0.0.1'
    PORT = '3306'
    DBNAME = 'app'
    SQLALCHEMY_DATABASE_URI= '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                           PORT, DBNAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = True
