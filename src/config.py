import os
import secrets

#environment variable
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration
class Config(object):
    DEBUG = False
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" +  os.path.join(basedir, "search.db") 
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #whoosh search 
    # WHOOSH_BASE = 'whoosh' + os.path.join(basedir, "search.db")
    WHOOSH_BASE = 'indexed'
    
class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
    
    
