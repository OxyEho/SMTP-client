import ssl
import socket
import os
import base64
import getpass

from client.file import File
from client.mail_creator import MailCreator


class Client:
    def __init__(self, login: str, to: str, subject: str, do_ssl: bool,
                 do_auth: bool, directory: str, do_verbose: bool, server: str):
        self.login = login
        self.to = to
        self.subject = subject
        self._do_ssl = do_ssl
        self._do_auth = do_auth
        self._directory = directory
        self._do_verbose = do_verbose
        if do_auth:
            self._password = self._get_password()
        self._commands = []
        self._port: int
        self._server: str
        self._set_server(server)
        self._set_commands()

    def _create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self._do_ssl:
            sock = ssl.wrap_socket(sock)
        return sock

    def _set_server(self, server_port: str):
        server_port = server_port.split(':')
        self._server = server_port[0]
        self._port = int(server_port[1])

    def _set_commands(self):
        if self._do_auth:
            self._commands = [f'EHLO {self.login.replace("@", ".")}\n', 'auth login\n',
                              f'{base64.b64encode(self.login.encode("utf-8")).decode("utf-8")}\n',
                              f'{base64.b64encode(self._password.encode("utf-8")).decode("utf-8")}\n',
                              f'MAIL FROM: <{self.login}>\nrcpt to: <{self.to}>\nDATA\n']
        else:
            self._commands = [f'EHLO {self.login.replace("@", ".")}\n',
                              f'MAIL FROM: {self.login}\n',
                              f'rcpt to: {self.to}\n',
                              'DATA\n']

    @staticmethod
    def _get_password():
        return getpass.getpass()

    def get_images(self):
        return [File(self._directory + x) for x in os.listdir(self._directory) if self._check_jpg(x)]

    @staticmethod
    def _check_jpg(name: str) -> bool:
        return name.endswith('.jpg')

    def _make_mail(self) -> str:
        mail_creator = MailCreator()
        mail_creator.add_header(self.login, self.to, self.subject)
        files = self.get_images()
        for i, file in enumerate(files):
            if i == len(files) - 1:
                mail_creator.add_content(file, True)
            else:
                mail_creator.add_content(file)
        return mail_creator.get_result_mail()

    def run(self):
        sock = self._create_socket()
        try:
            sock.connect((self._server, self._port))
            print(sock.recv(1024).decode('utf-8'))
            for el in self._commands:
                sock.send(el.encode())
                print(sock.recv(1024).decode('utf-8'))
                if 'DATA' in el:
                    sock.send(self._make_mail().encode())
                    print(sock.recv(1024).decode('utf-8'))
        finally:
            sock.close()
