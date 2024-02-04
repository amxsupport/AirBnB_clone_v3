#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
import os
app = Flask(__name__)


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all('Amenity')
    amenities_list = []
    for amenity in amenities.values():
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list), 200


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id=None):
    """Retrieves a Amenity object with the id linked to it"""
    amenities = storage.all('Amenity')
    amenity = amenities.get('Amenity' + "." + amenity_id)
    if amenity is None:
        abort(404)
    else:
        return jsonify(amenity.to_dict()), 200


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id=None):
    """Deletes a Amenity object"""
    obj = storage.get('Amenity', amenity_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return jsonify({}), 200

