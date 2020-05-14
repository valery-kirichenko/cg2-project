from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from .models.user import User
from .models.following import Following


class Follow(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('username', required=True, help='Username parameter is required to perform this action')
        args = parser.parse_args()

        r1 = User.find_by_field('username', get_jwt_identity())

        following = Following(
            _routing=r1.hits[0].meta.id,
            user_from=r1.hits[0].username,
            user_to=args['username'])
        try:
            following.save()
        except ValueError as err:
            return {'msg': str(err)}, 422

        return {'msg': 'ok'}

    @jwt_required
    def delete(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('username', required=True, help='Username parameter is required to perform this action')
        args = parser.parse_args()

        followings = Following.find(get_jwt_identity(), args['username'])
        if followings.hits.total.value == 0:
            return {'msg': 'Already not following'}, 422

        for following in followings:
            following.delete()

        return {'msg': 'ok'}

    @jwt_required
    def get(self):
        username = request.args.get('username')
        if username is None:
            return {'msg': 'Username parameter is required to perform this action'}, 400

        return {'msg': 'ok', 'is_following': Following.is_following(get_jwt_identity(), username)}
