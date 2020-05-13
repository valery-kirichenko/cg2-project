from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from elasticsearch_dsl import connections

from api.auth.register import Register
from api.auth.login import Login
from api.beeper import Beeper, BeeperById
from api.follow import Follow
from api.feed import GeneralFeed, PersonalFeed, UsersFeed
from api.search import BeepSearch

app = Flask(__name__)
app.config.from_pyfile('config.py')
jwt = JWTManager(app)

connections.create_connection(hosts=[app.config['ELASTIC_ADDRESS']])

api = Api(app)
api.add_resource(Register, '/api/auth/register')
api.add_resource(Login, '/api/auth/login')
api.add_resource(Beeper, '/api/beep')
api.add_resource(BeeperById, '/api/beep/<beep_id>')
api.add_resource(Follow, '/api/follow')
api.add_resource(GeneralFeed, '/api/feed/all')
api.add_resource(PersonalFeed, '/api/feed/')
api.add_resource(UsersFeed, '/api/feed/<username>')
api.add_resource(BeepSearch, '/api/search/beep')

# enable CORS
CORS(app, resources={r'/api/*': {'origins': '*'}})


@app.cli.command("migrate")
def migrate():
    from api.models.user import User
    from api.models.beep import Beep
    from api.models.following import Following

    User.init()
    Beep.init()
    Following.init()


if __name__ == '__main__':
    app.run()
