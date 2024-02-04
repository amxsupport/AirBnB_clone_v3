#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.state import City
from models.city import City
from models.place import Place
import os
app = Flask(__name__)


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id=None):
    """Retrieves the list of all Place objects for a city"""
    cities = storage.all('City')
    city = cities.get('City' + '.' + city_id)
    if city is None:
        abort(404)
    places_list = []
    places = storage.all('Place')
    for place in places.values():
        if place.city_id == city_id:
            places_list.append(place.to_dict())
    return jsonify(places_list), 200



