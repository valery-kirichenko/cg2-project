from flask_restful import Resource, reqparse

from ..models.user import User


parser = reqparse.RequestParser(trim=True)
parser.add_argument('username', required=True, help='Username parameter is required to perform this action')
parser.add_argument('password', required=True, help='Password parameter is required to perform this action')


class Register(Resource):
    def post(self):
        args = parser.parse_args()

        user = User(username=args['username'], access_level=0x01)
        user.hash_password(args['password'])
        try:
            user.save()
            return {'message': 'ok'}
        except ValueError as e:
            return {'message': str(e)}, 422
