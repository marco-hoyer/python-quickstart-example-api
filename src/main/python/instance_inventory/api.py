import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_restful import Api
from instance_inventory.resource.instances import Instance, Instances

app = Flask(__name__)
api = Api(app)


# set app secret to something considered random from os
app.secret_key = os.urandom(24)


# api resources
api.add_resource(Instances, '/instances')
api.add_resource(Instance, '/instances/<string:instance_id>')


def init_access_log(access_log_file):
    logger = logging.getLogger('werkzeug')
    handler = RotatingFileHandler(access_log_file, maxBytes=10000, backupCount=5)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def run(bind, port, debug, access_log_file=False):
    if access_log_file:
        init_access_log(access_log_file)
    app.run(bind, port, threaded=True, debug=debug)


if __name__ == '__main__':
    run(bind='127.0.0.1', port=8080, debug=True)