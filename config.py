import os

#environment variable
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "myseckey12345"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" +  os.path.join(basedir, "search.db") 
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #whoosh search 
    WHOOSH_BASE = 'whoosh' + os.path.join(basedir, "search.db")
    
    
