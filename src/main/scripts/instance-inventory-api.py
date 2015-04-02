import argparse
from instance_inventory import api


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', help="Bind address (0.0.0.0 f.e.)", type=str, default='0.0.0.0')
    parser.add_argument('--port', help="Port to bind on", type=int, default=8080)
    parser.add_argument('--debug', help="Synchronisiere alle Shops", action="store_true", default=False)
    return parser.parse_args()


def main():
    args = parse_arguments()
    api.run(args.bind, args.port, args.debug)

main()