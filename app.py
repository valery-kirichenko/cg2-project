from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from elasticsearch_dsl import connections

from api.auth.register import Register
from api.auth.login import Login
from api.beeper import Beeper, BeeperById


app = Flask(__name__)
app.config.from_pyfile('config.py')
jwt = JWTManager(app)

connections.create_connection(hosts=[app.config['ELASTIC_ADDRESS']])

api = Api(app)
api.add_resource(Register, '/api/auth/register')
api.add_resource(Login, '/api/auth/login')
api.add_resource(Beeper, '/api/beep')
api.add_resource(BeeperById, '/api/beep/<beep_id>')

# enable CORS
CORS(app, resources={r'/api/*': {'origins': '*'}})


@app.cli.command("migrate")
def migrate():
    from api.models.user import User
    from api.models.beep import Beep

    User.init()
    Beep.init()


if __name__ == '__main__':
    app.run()

