
from src.app import  db, ma
#import flask_whooshalchemy as wa
from datetime import datetime

#Models

class Movies(db.Model):
    
    __tablename__ = 'Movies'
    __table_args__ = {'extend_existing': True}
    __searchable__ = ['title', 'year', 'genre', 'description', 'producer']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)
    producer = db.Column(db.String(30), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Title {}>'.format(self.title)
                    
class MovieSchema(ma.Schema):
    class Meta:
        # model = Movies
        # extend_existing=True
        fields = ('id', 'title', 'year', 'genre', 'description', 'producer')
        
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)



##creating whoosh index as commented 
#wa.whoosh_index(app, PostData)

#programmatic creating database
#db.create_all()