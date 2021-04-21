from client.file import File


class MailCreator:
    def __init__(self):
        self._result_mail = ''

    def add_header(self, from_usr: str, to_usr: str, subject: str):
        self._result_mail += f'From: {from_usr}\nTo: {to_usr}\nSubject: {subject}'
        self._result_mail += '\nContent-type: multipart/mixed; boundary=a'

    def add_content(self, file: File, is_last: bool = False):
        self._result_mail += '\n\n--a'
        self._result_mail += f'\nMime-Version: 1.0'
        self._result_mail += f'\nContent-Type: image/jpeg; name="=?UTF-8?B?{file.base64_name}?="'
        self._result_mail += f'\nContent-Disposition: attachment; filename="=?UTF-8?B?{file.base64_name}?="'
        self._result_mail += '\nContent-Transfer-Encoding: base64\n\n'
        self._result_mail += file.get_base64()
        if is_last:
            self._result_mail += '\n--a--'
            self._result_mail += '\n.\n'
        else:
            self._result_mail += '\n--a'

    def get_result_mail(self) -> str:
        return self._result_mail

