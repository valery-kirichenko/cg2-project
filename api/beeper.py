from elasticsearch import NotFoundError
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from .models.beep import Beep


class Beeper(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('text', required=True, help='Text parameter is required to perform this action')
        args = parser.parse_args()

        beep = Beep(text=args['text'], username=get_jwt_identity())
        beep.save()

        return {'msg': 'ok', 'beep_id': beep.meta.id}


class BeeperById(Resource):
    def get(self, beep_id):
        try:
            beep = Beep.get(id=beep_id)
            return {'text': beep.text, 'date': str(beep.date), 'username': beep.username}
        except NotFoundError:
            return {'msg': 'not found'}, 404
