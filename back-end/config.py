import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
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
    POSTS_PER_PAGE = 10
    USERS_PER_PAGE = 10
    COMMENTS_PER_PAGE = 10
    MESSAGES_PER_PAGE = 10
    ADMINS = ['836282264@qq.com']  # 管理员的邮箱地址
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SENDER = os.environ.get('MAIL_SENDER')
    LANGUAGES = ['zh', 'en']