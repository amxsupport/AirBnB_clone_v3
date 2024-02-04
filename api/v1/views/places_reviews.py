#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State
from models.state import City
from models.city import City
from models.place import Place
from models.review import Review
import os
app = Flask(__name__)


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id=None):
    """Retrieves the list of all Reviews for a place"""
    places = storage.all('Place')
    place = places.get('Place' + '.' + place_id)
    if place is None:
        abort(404)
    reviews_list = []
    reviews = storage.all('Review')
    for review in reviews.values():
        if review.place_id == place_id:
            reviews_list.append(review.to_dict())
    return jsonify(reviews_list), 200


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id=None):
    """Retrieves a Review object with the id linked to it"""
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    else:
        return jsonify(review.to_dict()), 200


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id=None):
    """Deletes a Review object"""
    obj = storage.get('Review', review_id)
    if obj is None:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
    return jsonify({}), 200



