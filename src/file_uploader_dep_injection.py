from typing import Protocol
import requests


class FileUploader(Protocol):
    def upload_file(self, file_path: str) -> dict: ...


class FileIOUploader:
    API_URL = "https://file.io"

    def upload_file(self, file_path: str) -> dict:
        with open(file_path, "rb") as file:
            response = requests.post(self.API_URL, files={"file": file})
        return response.json()


def process_file_upload(file_path: str, uploader: FileUploader):
    response = uploader.upload_file(file_path)
    return response
