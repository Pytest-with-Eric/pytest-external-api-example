from src.file_uploader_di import upload_file, download_file


class FakeFileUploadAPI:
    def __init__(self):
        self.uploaded_files = {}

    def upload_file(self, file_name):
        # Simulate a successful upload response
        response = {
            "success": True,
            "link": f"https://file.io/{file_name}",
            "name": file_name,
        }
        self.uploaded_files[file_name] = response
        return response

    def download_file(self, download_link, file_name):
        # Simulate a successful download by creating a placeholder response
        if file_name in self.uploaded_files:
            print(f"Fake downloaded {file_name} successfully.")
        else:
            raise FileNotFoundError("File not found in uploaded files.")


def test_upload_file_with_dependency_injection():
    file_name = "sample.txt"
    expected_response = {
        "success": True,
        "link": f"https://file.io/{file_name}",
        "name": file_name,
    }
    fake_api = FakeFileUploadAPI()  # Inject the fake API

    response = upload_file(file_name, fake_api)

    assert response == expected_response
    assert file_name in fake_api.uploaded_files


def test_download_file_with_dependency_injection():
    file_name = "sample.txt"
    fake_api = FakeFileUploadAPI()

    # First, upload the file so it's available for download
    fake_api.upload_file(file_name)

    # Now, download the file using the injected fake API
    download_file(f"https://file.io/{file_name}", file_name, fake_api)
    assert file_name in fake_api.uploaded_files
