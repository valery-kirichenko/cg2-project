import os

from flask import Blueprint, send_file

ui = Blueprint('web', __name__, static_folder='./dist/static')


@ui.route('/', defaults={'path': ''})
@ui.route('/<path:path>')
def catch_all(path):
    dist_dir = os.path.join(os.path.dirname(__file__), 'dist')
    return send_file(os.path.join(dist_dir, 'index.html'))
