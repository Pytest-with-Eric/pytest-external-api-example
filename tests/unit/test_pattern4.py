"""Pattern 4: Dependency Injection"""

from unittest import mock
from src.file_uploader_dep_injection import process_file_upload, FileIOUploader


def test_process_file_upload():
    file_name = "sample.txt"
    file_io_uploader = FileIOUploader()
    response = process_file_upload(file_path=file_name, uploader=file_io_uploader)
    assert response["success"] is True
    assert response["name"] == file_name
    assert response["key"] is not None


def test_process_file_upload_mock():
    mock_uploader = mock.Mock()
    mock_uploader.upload_file.return_value = {
        "success": True,
        "link": "https://file.io/abc123",
    }

    result = process_file_upload("test.txt", uploader=mock_uploader)
    assert result["success"] is True
    assert result["link"] == "https://file.io/abc123"
    mock_uploader.upload_file.assert_called_once_with("test.txt")
