from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from .models.beep import Beep
from .models.following import Following


def search_with_users(username):
    return Beep.search().query('match', username=username).sort({"date": {"order": "desc"}})


def generate_response(search, offset):
    return [
        {'text': hit.text, 'username': hit.username, 'date': hit.date.isoformat(), 'id': hit.meta.id}
        for hit in search[offset:offset + 10]
    ]


class GeneralFeed(Resource):
    def get(self):
        offset = request.args.get('offset', default=0, type=int)
        s = Beep.search().sort({"date": {"order": "desc"}})
        return {'msg': 'ok',
                'beeps': generate_response(s, offset)}


class PersonalFeed(Resource):
    @jwt_required
    def get(self):
        followings = ' '.join(Following.get_followings(get_jwt_identity()))
        offset = request.args.get('offset', default=0, type=int)
        s = search_with_users(followings)
        return {'msg': 'ok',
                'beeps': generate_response(s, offset)}


class UsersFeed(Resource):
    def get(self, username):
        offset = request.args.get('offset', default=0, type=int)
        s = search_with_users(username)
        return {'msg': 'ok',
                'beeps': generate_response(s, offset)}
