from flask import Flask
from flask_restplus import Api
from firebase_admin import initialize_app, credentials, firestore

# create db using server
cred = credentials.Certificate('./python-44e42-3b80ec18c6f3.json')
initialize_app(cred)
db = firestore.client()

# flask and flask-restplus initialization
app = Flask(__name__)
api = Api(app)

from app import routes