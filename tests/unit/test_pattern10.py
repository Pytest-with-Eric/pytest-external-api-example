from src.file_uploader import upload_file_param
import pytest
from wiremock.testing.testcontainer import wiremock_container
from wiremock.constants import Config
from wiremock.client import *


@pytest.fixture
def wiremock_server():
    # Set up WireMock server with mappings
    with wiremock_container(secure=False) as wm:
        # Set base URL for WireMock admin (only for WireMock setup purposes)
        Config.base_url = wm.get_url("__admin")

        # Map the upload endpoint for a successful response
        Mappings.create_mapping(
            Mapping(
                request=MappingRequest(method=HttpMethods.POST, url="/"),
                response=MappingResponse(
                    status=200,
                    json_body={
                        "success": True,
                        "link": "https://file.io/TEST",
                        "key": "TEST",
                        "name": "sample.txt",
                    },
                ),
                persistent=False,
            )
        )

        yield wm  # Yield the WireMock instance for the tests


def test_upload_file_success(wiremock_server):
    response = upload_file_param("sample.txt", wiremock_server.get_url("/"))

    assert response["success"] is True
    assert response["link"] == "https://file.io/TEST"
    assert response["name"] == "sample.txt"
    assert response["key"] == "TEST"
