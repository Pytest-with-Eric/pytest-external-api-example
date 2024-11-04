class FakeFileUploadAPI:
    def __init__(self):
        self.uploaded_files = {}

    def upload_file(self, file_name):
        response = {
            "success": True,
            "link": f"https://file.io/{file_name}",
            "name": file_name,
        }
        self.uploaded_files[file_name] = response
        return response

    def __contains__(self, file_name):
        return file_name in self.uploaded_files


def test_upload_file_with_fake():
    file_name = "sample.txt"
    expected_response = {
        "success": True,
        "link": f"https://file.io/{file_name}",
        "name": file_name,
    }
    api = FakeFileUploadAPI()

    response = api.upload_file(file_name)

    assert response == expected_response
    assert file_name in api
