from pathlib import Path
from src.file_uploader import upload_file, download_file


def test_upload_file():
    file_name = "sample.txt"
    response = upload_file(file_name)
    assert response["success"] is True
    assert response["name"] == file_name
    assert response["key"] is not None


def test_upload_download_file():
    file_name = "sample.txt"
    response = upload_file(file_name)
    download_link = response["link"]
    download_file(download_link, file_name)
    downloaded_file = Path(file_name)
    assert downloaded_file.exists()
