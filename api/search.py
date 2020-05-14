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

        s = Beep.search().query('match', text=text).source(['*'])
        r = s.execute()
        return [{'text': hit.text, 'date': str(hit.date), 'username': hit.username} for hit in r]


class Suggestion(Resource):
    def get(self):
        text = request.args.get('text')
        if text is None:
            return {'msg': 'Text parameter is required to perform this action'}, 400
        if len(text) < 3:
            return {'msg': 'Too short text for search'}, 422

        s = Beep.search().suggest('suggestion', text, term={'field': 'username'})
        r = s.execute()
        suggestions = [{'text': option['text'], 'score': option['score']}
               for term in r.suggest.suggestion for option in term['options']]
        sorted_suggestions = sorted(suggestions, key=lambda x: x['score'], reverse=True)
        return [suggestion['text'] for suggestion in sorted_suggestions]
