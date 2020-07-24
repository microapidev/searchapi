from whoosh.analysis import SimpleAnalyzer
from api import db, app, ma
import flask_whooshalchemy as wa

#Models







##creating whoosh index as commented 
#wa.whoosh_index(app, PostData)

#programmatic creating database
db.create_all()
