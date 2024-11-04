import requests


class FileIOAdapter:
    API_URL = "https://file.io"

    def upload_file(self, file_path):
        with open(file_path, "rb") as file:
            response = requests.post(self.API_URL, files={"file": file})
        return response.json()
