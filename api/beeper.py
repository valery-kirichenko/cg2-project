from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from elasticsearch_dsl import *
from .models.beep import Beep


class Beeper(Resource):
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('text', required=True, help='Text parameter is required to perform this action')
        args = parser.parse_args()

        beep = Beep(text=args['text'], username=get_jwt_identity())
        beep.save()

        s = Beep.search()
        for hit in s.scan():
            print(hit.date)


        return {'message': 'ok', 'beep_id': beep.meta.id}

