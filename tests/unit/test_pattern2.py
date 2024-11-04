"""Pattern 2 - Mock the Request Library"""

from unittest.mock import patch, Mock, ANY
from src.file_uploader import upload_file


def test_upload_file():
    file_name = "sample.txt"
    stub_upload_response = {
        "success": True,
        "link": "https://file.io/TEST",
        "key": "TEST",
        "name": file_name,
    }

    with patch("src.file_uploader.requests.post") as mock_post:
        mock_post_response = Mock()
        mock_post_response.status_code = 200
        mock_post_response.json.return_value = stub_upload_response
        mock_post.return_value = mock_post_response

        response = upload_file(file_name)

        assert response["success"] is True
        assert response["link"] == "https://file.io/TEST"
        assert response["name"] == file_name
        mock_post.assert_called_once_with("https://file.io", files={"file": ANY})
