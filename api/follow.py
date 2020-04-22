from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from .models.user import User
from .models.following import Following


class Follow(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('user_to', required=True, help='User_to parameter is required to perform this action')
        args = parser.parse_args()

        r1 = User.find_by_field('username', get_jwt_identity())

        following = Following(
            _routing=r1.hits[0].meta.id,
            user_from=r1.hits[0].username,
            user_to=args['user_to'])
        try:
            following.save()
        except ValueError as err:
            return {'msg': str(err)}, 422

        return {'msg': 'ok'}
