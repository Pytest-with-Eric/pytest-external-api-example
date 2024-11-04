"""Pattern 5: Dependency Injection + Fake - Create a Fake Object and Inject It"""

from src.file_uploader_dep_injection import process_file_upload


class FakeFileIOUploader:
    def __init__(self):
        self.uploaded_files = {}

    def upload_file(self, file_path: str) -> dict:
        # Simulate uploading by "saving" the file's path in a dictionary
        self.uploaded_files[file_path] = f"https://file.io/fake-{file_path}"
        return {"success": True, "link": self.uploaded_files[file_path]}


def test_process_file_upload_with_fake():
    fake_uploader = FakeFileIOUploader()
    result = process_file_upload("test.txt", uploader=fake_uploader)

    assert result["success"] is True
    assert result["link"] == "https://file.io/fake-test.txt"
    assert "test.txt" in fake_uploader.uploaded_files
