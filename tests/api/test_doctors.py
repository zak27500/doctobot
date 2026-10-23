import pytest
from fastapi.testclient import TestClient

DOCTOR = {"name": "House", "middlename": "Gregory", "specialty": "general"}


def test_create_doctor_returns_201_with_id(client: TestClient) -> None:
    response = client.post("/doctors", json=DOCTOR)

    assert response.status_code == 201
    assert response.json() == {"id": 1, **DOCTOR}


def test_created_doctor_can_be_retrieved(client: TestClient) -> None:
    created = client.post("/doctors", json=DOCTOR).json()

    response = client.get(f"/doctors/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


@pytest.mark.parametrize("specialty", ["general", "surgeon", "optician"])
def test_create_doctor_accepts_every_specialty(client: TestClient, specialty: str) -> None:
    response = client.post("/doctors", json={**DOCTOR, "specialty": specialty})

    assert response.status_code == 201
    assert response.json()["specialty"] == specialty


def test_create_doctor_with_unknown_specialty_returns_422(client: TestClient) -> None:
    response = client.post("/doctors", json={**DOCTOR, "specialty": "dentist"})

    assert response.status_code == 422


@pytest.mark.parametrize("field", ["name", "middlename", "specialty"])
def test_create_doctor_with_missing_field_returns_422(client: TestClient, field: str) -> None:
    payload = {key: value for key, value in DOCTOR.items() if key != field}

    response = client.post("/doctors", json=payload)

    assert response.status_code == 422


def test_create_doctor_ignores_client_supplied_id(client: TestClient) -> None:
    response = client.post("/doctors", json={**DOCTOR, "id": 42})

    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_list_doctors(client: TestClient) -> None:
    client.post("/doctors", json=DOCTOR)
    client.post("/doctors", json={**DOCTOR, "name": "Yang", "specialty": "surgeon"})

    response = client.get("/doctors")

    assert response.status_code == 200
    assert [doctor["name"] for doctor in response.json()] == ["House", "Yang"]


def test_list_doctors_when_empty(client: TestClient) -> None:
    response = client.get("/doctors")

    assert response.status_code == 200
    assert response.json() == []


def test_get_unknown_doctor_returns_404(client: TestClient) -> None:
    response = client.get("/doctors/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Doctor not found"}
