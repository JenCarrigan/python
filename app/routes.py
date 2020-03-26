from app import app, api
from flask_restplus import Resource

@api.route('/')
class Hello(Resource):
  def get(self):
    return {'hello': 'world'}