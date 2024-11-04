import requests


def upload_file(file_name):
    with open(file_name, "rb") as file:
        response = requests.post("https://file.io", files={"file": file})
        response.raise_for_status()
        upload_data = response.json()

        if response.status_code == 200 and upload_data.get("success"):
            print(f"File uploaded successfully. Upload data: {upload_data}")
            return upload_data
        else:
            raise Exception("File upload failed.")


# def download_file(download_link, file_name):
#     response = requests.get(download_link)
#     response.raise_for_status()
#     output_file_name = f"download__{file_name}"

#     with open(output_file_name, "wb") as output_file:
#         output_file.write(response.content)
#     print(f"File downloaded successfully as {output_file_name}")
