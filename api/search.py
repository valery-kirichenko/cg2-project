from flask import request
from flask_restful import Resource

from api.models.beep import Beep


class BeepSearch(Resource):
    def get(self):
        text = request.args.get('text')
        if text is None:
            return {'msg': 'Text parameter is required to perform this action'}, 400
        if len(text) < 2:
            return {'msg': 'Too short text for search'}, 422

        s = Beep.search().query('match', text=text)
        r = s.execute()
        return [hit.meta.id for hit in r]
