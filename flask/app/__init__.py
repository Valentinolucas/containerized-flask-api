from flask import Flask 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# app config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

from app import views