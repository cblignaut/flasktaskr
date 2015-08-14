import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = """\xc2\xec\xc0L\x0b\x02e;<MB\xf7:)\xea\xd4\xab\xb5\xe1\x82K\xa6_\x17"""  
