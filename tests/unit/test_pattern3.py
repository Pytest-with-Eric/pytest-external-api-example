"""Pattern 3 - Create an Adaptor Class and Mock It"""

from unittest import mock
from src.file_uploader_adaptor import FileIOAdapter


def test_upload_file():
    with mock.patch(
        "src.file_uploader_adaptor.FileIOAdapter.upload_file"
    ) as mock_upload_file:
        mock_upload_file.return_value = {"success": True}

        adapter = FileIOAdapter()
        response = adapter.upload_file("sample.txt")

        assert response == {"success": True}
        mock_upload_file.assert_called_once_with("sample.txt")
