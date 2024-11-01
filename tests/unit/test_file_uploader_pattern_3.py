from unittest import mock
from src.file_uploader import FileUploadAPI


def test_upload_file():
    file_name = "sample.txt"
    expected_response = {
        "success": True,
        "link": "https://file.io/TEST",
        "key": "TEST",
        "name": file_name,
    }
    with mock.patch(
        "src.file_uploader.FileUploadAPI.upload_file", return_value=expected_response
    ) as mock_upload:
        api = FileUploadAPI()
        response = api.upload_file(file_name)

        assert response == expected_response
        mock_upload.assert_called_once_with(file_name)
