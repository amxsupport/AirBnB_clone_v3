#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.place import Place
import os
app = Flask(__name__)


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenity_for_place(place_id=None):
    """Retrieves the list of all Amenity objects for a place"""
    place_object = storage.get("Place", place_id)
    if place_object is None:
        return jsonify({}), 404
    amenities_list = []
    for amenity in place_object.amenities:
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list), 200



