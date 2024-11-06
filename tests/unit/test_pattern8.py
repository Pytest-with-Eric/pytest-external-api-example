import vcr
from src.file_uploader import upload_file


@vcr.use_cassette("tests/cassettes/upload_file.yaml")
def test_upload_file():
    file_name = "sample.txt"

    response = upload_file(file_name)

    assert response["success"] is True
    assert response["name"] == file_name
    assert response["key"] is not None
