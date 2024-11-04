"""Pattern 1 - Full Integration Test"""

from src.file_uploader import upload_file


def test_upload_file():
    file_name = "sample.txt"
    response = upload_file(file_name)
    assert response["success"] is True
    assert response["name"] == file_name
    assert response["key"] is not None
