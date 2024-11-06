"""Pattern 6: Mocking external API calls using responses library"""

import responses
from src.file_uploader import upload_file


# Test cases
@responses.activate
def test_upload_file_success():
    # Mock the successful response from file.io
    responses.add(
        responses.POST,
        "https://file.io",
        json={"success": True, "link": "https://file.io/abc123"},
        status=200,
    )

    # Call the function and verify the response
    result = upload_file("sample.txt")
    assert result == {"success": True, "link": "https://file.io/abc123"}
    assert responses.calls[0].response.status_code == 200
