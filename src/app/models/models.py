from src.app import db, ma
from flask import Flask
import src.flask_whooshalchemy as wa
from datetime import datetime
from marshmallow import Schema, fields
from flask_restx import fields as restx_fields



# Models

class Movies(db.Model):
    __tablename__ = 'Movies'
    __table_args__ = {'extend_existing': True}
    __searchable__ = ['title', 'year', 'genre', 'description', 'producer']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.String(4), nullable=True)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)
    producer = db.Column(db.String(30), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Movies(title={self.title!r})>".format(self=self)


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    year = fields.Str()
    genre = fields.Str()
    description = fields.Str()
    producer = fields.Str()
    created = fields.DateTime()

    # class Meta:
    #     # model = Movies
    #     # extend_existing=True
    #     fields = ('id', 'title', 'genre', 'description', 'producer')


movie_schema = MovieSchema(many=True)
# movies_schema = MovieSchema(many=True)


# Flask-restx api models
def create_api_movie_model(flaskapi):
    movie = flaskapi.model('Movie', {
        'title': restx_fields.String(required=True, description='The Title of the movie'),
        'year': restx_fields.String(required=True, description='The Year the movie was produced'),
        'genre': restx_fields.String(required=True, description='The Genre of the movie'),
        'description': restx_fields.String(required=True, description='The description of the movie'),
        'producer': restx_fields.String(required=True, description='The producer of the movie')
    })
    return movie

def create_api_search_model(flaskapi):
    search = flaskapi.model('Search', {
        'search': restx_fields.String(required=True, description='The string to search')
    })
    return search
##creating whoosh index as commented
# wa.whoosh_index(app, Movies)

# programmatic creating database
# db.create_all()
