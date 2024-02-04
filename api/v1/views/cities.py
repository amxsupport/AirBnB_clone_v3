#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.state import City
from models.city import City
import os
app = Flask(__name__)


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id=None):
    """Retrieves the list of all City objects"""
    states = storage.all('State')
    state = states.get('State' + '.' + state_id)
    if state is None:
        abort(404)
    city_list = []
    cities = storage.all('City')
    for city in cities.values():
        if city.state_id == state_id:
            city_list.append(city.to_dict())
    return jsonify(city_list), 200


