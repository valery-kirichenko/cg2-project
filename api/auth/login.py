from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from ..models.user import User


parser = reqparse.RequestParser(trim=True)
parser.add_argument('username', required=True, help='Username parameter is required to perform this action')
parser.add_argument('password', required=True, help='Password parameter is required to perform this action')


class Login(Resource):
    def post(self):
        args = parser.parse_args()

        r = User.find_users(args['username'])
        if r.hits.total.value == 0:
            return {'msg': 'User not found'}, 401
        user = r.hits[0]
        if not user.verify_password(args['password']):
            return {'msg': 'Wrong password'}, 401
        return {'msg': 'ok', 'token': create_access_token(identity=args['username'])}
