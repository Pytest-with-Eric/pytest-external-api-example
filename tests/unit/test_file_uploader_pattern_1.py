from pathlib import Path
from src.file_uploader import upload_file, download_file


def test_upload_download_file():
    file_name = "sample.txt"

    # Act: Upload the file to get a download link
    response = upload_file(file_name)
    download_link = response["link"]

    # Act: Download the file
    download_file(download_link, file_name)

    # Assert the downloaded file exists and has content
    downloaded_file = Path(file_name)
    assert downloaded_file.exists()
