from unittest.mock import patch, Mock, ANY
from src.file_uploader import upload_file, download_file


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


def test_upload_and_download_file():
    file_name = "sample.txt"
    stub_upload_response = {
        "success": True,
        "link": "https://file.io/TEST",
        "key": "TEST",
        "name": file_name,
    }
    stub_file_content = b"This is the content of the downloaded file."

    with patch("src.file_uploader.requests.post") as mock_post, patch(
        "src.file_uploader.requests.get"
    ) as mock_get:

        # Mock upload response
        mock_post_response = Mock()
        mock_post_response.status_code = 200
        mock_post_response.json.return_value = stub_upload_response
        mock_post.return_value = mock_post_response

        # Upload file and get response
        upload_response = upload_file(file_name)
        assert upload_response["success"] is True
        assert upload_response["link"] == "https://file.io/TEST"
        mock_post.assert_called_once_with("https://file.io", files={"file": ANY})

        # Mock download response
        mock_get_response = Mock()
        mock_get_response.status_code = 200
        mock_get_response.content = stub_file_content
        mock_get.return_value = mock_get_response

        # Download file
        download_file(upload_response["link"], file_name)
        mock_get.assert_called_once_with("https://file.io/TEST")

        # Assert the file was saved with correct content
        with open(f"download__{file_name}", "rb") as downloaded_file:
            assert downloaded_file.read() == stub_file_content
