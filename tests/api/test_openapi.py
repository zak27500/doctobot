from fastapi.testclient import TestClient


def test_root_redirects_to_swagger_ui(client: TestClient) -> None:
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/docs"


def test_swagger_ui_is_served(client: TestClient) -> None:
    response = client.get("/docs")

    assert response.status_code == 200


def test_openapi_schema_exposes_routes(client: TestClient) -> None:
    paths = client.get("/openapi.json").json()["paths"]

    assert set(paths) == {
        "/doctors",
        "/doctors/{doctor_id}",
        "/patients",
        "/patients/{patient_id}",
    }
