import requests


def upload_file(file_name):
    with open(file_name, "rb") as file:
        response = requests.post("https://file.io", files={"file": file})
        response.raise_for_status()
        upload_data = response.json()

        if response.status_code == 200:
            print(f"File uploaded successfully. Upload data: {upload_data}")
            return upload_data
        else:
            raise Exception("File upload failed.")


def upload_file_param(file_name, base_url):
    with open(file_name, "rb") as file:
        response = requests.post(base_url, files={"file": file})
        response.raise_for_status()
        upload_data = response.json()

        if response.status_code == 200:
            print(f"File uploaded successfully. Upload data: {upload_data}")
            return upload_data
        else:
            raise Exception("File upload failed.")
