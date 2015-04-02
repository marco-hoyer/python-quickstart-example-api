from flask import Flask
from flask_restful import Api
from instance_inventory.resource.instances import Instance, Instances

app = Flask(__name__)
api = Api(app)

api.add_resource(Instances, '/instances')
api.add_resource(Instance, '/instances/<string:instance_id>')


def run(bind, port, debug):
    app.run(bind, port, threaded=True, debug=debug)


if __name__ == '__main__':
    run(bind='0.0.0.0', port=8080, debug=True)