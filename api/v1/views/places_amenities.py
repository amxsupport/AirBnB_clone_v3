#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.place import Place
import os
app = Flask(__name__)



