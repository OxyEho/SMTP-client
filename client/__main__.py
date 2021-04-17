import argparse

from client.file import File
from client.mail_creator import MailCreator
from client.smtp_client import Client

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', type=str, default='<>')
    # arg_parser.add_argument('--password', type=str)
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
    # print(client.make_mail())
    # mail_creator = MailCreator()
    # mail_creator.add_header('valera808@inbox.ru', 'valera808@inbox.ru', 'Happy Pictures')
    # mail_creator.add_content(File('pic/1.jpg'))
    # print(mail_creator.get_result_mail())
