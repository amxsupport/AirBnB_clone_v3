#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
import os
app = Flask(__name__)

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all('State')
    state_list = []
    for state in states.values():
        state_list.append(state.to_dict())
    return jsonify(state_list), 200

