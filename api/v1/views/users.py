#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.user import User
import os
app = Flask(__name__)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all('User')
    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list), 200


