"""Pattern 4: Dependency Injection - Inject a Mock Uploader Object"""

from unittest import mock
from src.file_uploader_dep_injection import process_file_upload


def test_process_file_upload():
    mock_uploader = mock.Mock()
    mock_uploader.upload_file.return_value = {
        "success": True,
        "link": "https://file.io/abc123",
    }

    result = process_file_upload("test.txt", uploader=mock_uploader)
    assert result["success"] is True
    assert result["link"] == "https://file.io/abc123"
    mock_uploader.upload_file.assert_called_once_with("test.txt")
