from unittest.mock import patch, Mock, ANY
from src.file_uploader import upload_file


@patch("src.file_uploader.requests.post")
def test_upload_file_to_fileio(mock_post):
    # Arrange
    file_name = "sample.txt"
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "status": 200,
        "id": "716f5780-982c-11ef-90e0-0125ec1afe68",
        "key": "D6nO3e3yPgst",
        "path": "/",
        "nodeType": "file",
        "name": "sample.txt",
        "title": None,
        "description": None,
        "size": 39,
        "link": "https://file.io/D6nO3e3yPgst",
        "private": False,
        "expires": "2024-11-15T08:36:52.080Z",
        "downloads": 0,
        "maxDownloads": 1,
        "autoDelete": True,
        "planId": 0,
        "screeningStatus": "pending",
        "mimeType": "text/plain",
        "created": "2024-11-01T08:36:52.080Z",
        "modified": "2024-11-01T08:36:52.080Z",
    }
    mock_post.return_value = mock_response

    # Act
    response = upload_file(file_name)

    # Assert
    assert response["success"] is True
    assert response["key"] == "D6nO3e3yPgst"
    assert response["name"] == file_name
    mock_post.assert_called_once()
    mock_post.assert_called_with("https://file.io", files={"file": ANY})
