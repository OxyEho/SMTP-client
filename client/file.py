import base64


class File:
    def __init__(self, file_name: str):
        self.full_file_name = file_name
        self.file_name = file_name.split('/')[-1]
        self.base64_name = base64.b64encode(self.file_name.encode('utf-8')).decode('utf-8')

    def get_base64(self) -> str:
        with open(self.full_file_name, 'rb') as file:
            return base64.b64encode(file.read()).decode('utf-8')
