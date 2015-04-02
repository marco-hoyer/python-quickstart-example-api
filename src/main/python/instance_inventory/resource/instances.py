from flask_restful import Resource, reqparse

INSTANCES = {}

parser = reqparse.RequestParser()
parser.add_argument('hostname', type=str, help='Hostname of the instance', required=True)
parser.add_argument('fqdn', type=str, help='Fully qualified name', required=True)
parser.add_argument('ip', type=str, help='Instance IP address', required=True)
parser.add_argument('create_date', type=str, help='Instance IP address', required=True)


class Instance(Resource):
    def get(self, instance_id):
        try:
            return INSTANCES[instance_id]
        except KeyError:
            return 'Instance with instance_id: {0} does not exist!'.format(instance_id), 404

    def put(self, instance_id):
        if not INSTANCES.has_key(instance_id):
            return 'Instance with instance_id: {0} does not exist!'.format(instance_id), 404

        args = parser.parse_args(strict=True)
        INSTANCES[instance_id] = {'hostname': args['hostname'], 'fqdn': args['fqdn'], 'ip': args['ip']}
        return '', 201

    def post(self, instance_id):
        if INSTANCES.has_key(instance_id):
            return 'Instance with instance_id: {0} already exists!'.format(instance_id), 404

        args = parser.parse_args(strict=True)
        INSTANCES[instance_id] = {'hostname': args['hostname'], 'fqdn': args['fqdn'], 'ip': args['ip']}
        return '', 201

    def delete(self, instance_id):
        try:
            del INSTANCES[instance_id]
        except KeyError:
            return 'Instance with instance_id: {0} does not exist!'.format(instance_id), 404
        return '', 204


class Instances(Resource):
    def get(self):
        return INSTANCES