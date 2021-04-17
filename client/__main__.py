import argparse


from client.smtp_client import Client


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', type=str, default='<>')
    arg_parser.add_argument('-t', '--to', type=str)
    arg_parser.add_argument('-d', '--directory', type=str)
    arg_parser.add_argument('--subject', type=str, default='Happy pictures')
    arg_parser.add_argument('-s', '--server', type=str, default='smtp.mail.ru:25')
    arg_parser.add_argument('--ssl', action='store_true')
    arg_parser.add_argument('--auth', action='store_true')
    arg_parser.add_argument('-v', '--verbose', action='store_true')
    args = arg_parser.parse_args()
    client = Client(args.f, args.to, args.subject, args.ssl, args.auth, args.directory, args.verbose, args.server)
    client.run()
