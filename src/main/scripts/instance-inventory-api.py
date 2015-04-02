import argparse
from instance_inventory import api


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', help="Bind address (0.0.0.0 f.e.)", type=str, default='0.0.0.0')
    parser.add_argument('--port', help="Port to bind on", type=int, default=8080)
    parser.add_argument('--accesslog', help="Access log file", type=str, default=None)
    parser.add_argument('--debug', help="Enable flask debug mode with integrated debugger (Don't use this on public!)",
                        action="store_true", default=False)
    return parser.parse_args()


def main():
    args = parse_arguments()
    api.run(args.bind, args.port, args.debug, access_log_file=args.accesslog)

main()