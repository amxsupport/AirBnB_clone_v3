#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

app = Flask(__name__)

@app_views.route('/status')
def status():
    return jsonify({
                     "status": "OK"
                   })


