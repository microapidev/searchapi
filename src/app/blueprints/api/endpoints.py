from flask import Flask, render_template, jsonify, make_response, Blueprint
from flask_restx import Api
import flask_whooshalchemyplus as wa
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_restx import Resource, fields
from src.app.models.models import Movies, movie_schema, create_api_movie_model, create_api_search_model
from src.app import db

import json
import datetime



#Endpoints/routes
api = Blueprint('api', __name__)

# app.wsgi_app = ProxyFix(app.wsgi_app)
flaskapi = Api(api, doc='/docs', version='1.0', title='Search API', description='A simple movie search API')
ns = flaskapi.namespace('movie', description='Movie operations')
# db.create_all()

# register flask-restful

movie = create_api_movie_model(flaskapi)
search = create_api_search_model(flaskapi)

# @api.route("/hello")
# def index():
#     return "hello world"
#


@ns.route("")
class MovieList(Resource):
    ''' Let's you add a new movie to the db '''

    @ns.doc('get hello wold')
    def get(self):
        '''Gets all movies in the database'''
        results = Movies.query.all()
        all_movies = movie_schema.dump(results)
        return all_movies, 200


    @ns.doc('add movie to search index')
    @ns.response(500, "Some Fields are missing")
    @ns.response(201, "Created")
    @ns.expect(movie)
    # @ns.marshal_with(movie, 201)
    def post(self):
        '''Creates a new movie'''
        # db.session.add(Movies())
        try:
            data = flaskapi.payload

            title = data['title']
            genre = data['genre']
            description = data['description']
            year = data['year']
            producer = data['producer']
            db.session.add(Movies(title=title, year=year,  genre=genre, producer=producer, description=description))
            db.session.commit()

            return {"message": "Successfully Indexed"}, 201
        except KeyError as e:
            message = "The " + str(e) + " is required"
            return {"message": message}, 500
        except OSError as err:
            print(err)
            return {"message": "error"}, 500


@ns.route("/search")
class MovieSearch(Resource):
    '''To search for a particular movie'''

    @ns.doc('Search a movie')
    @ns.response(500, "Search Fields are missing")
    @ns.response(200, "Successful")
    @ns.expect(search)
    def post(self):
        try:
            search_query = flaskapi.payload

            results = Movies.query.whoosh_search(search_query['search']).all()
            all_movies_in_search = movie_schema.dump(results)
            return all_movies_in_search, 200
        except KeyError as e:
            message = "The " + str(e) + " is required"
            return {"message": message}, 500
