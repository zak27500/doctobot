from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient

PATIENT = {
    "name": "Dupont",
    "middlename": "Jean",
    "birthday": "1990-05-17",
    "email": "jean.dupont@example.com",
}


def test_create_patient_returns_201_with_id(client: TestClient) -> None:
    response = client.post("/patients", json=PATIENT)

    assert response.status_code == 201
    assert response.json() == {"id": 1, **PATIENT}


def test_created_patient_can_be_retrieved(client: TestClient) -> None:
    created = client.post("/patients", json=PATIENT).json()

    response = client.get(f"/patients/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_create_patient_born_today_is_accepted(client: TestClient) -> None:
    response = client.post("/patients", json={**PATIENT, "birthday": date.today().isoformat()})

    assert response.status_code == 201


def test_create_patient_with_future_birthday_returns_422(client: TestClient) -> None:
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    response = client.post("/patients", json={**PATIENT, "birthday": tomorrow})

    assert response.status_code == 422
    assert "birthday cannot be in the future" in response.text


def test_create_patient_with_invalid_email_returns_422(client: TestClient) -> None:
    response = client.post("/patients", json={**PATIENT, "email": "not-an-email"})

    assert response.status_code == 422


@pytest.mark.parametrize("field", ["name", "middlename", "birthday", "email"])
def test_create_patient_with_missing_field_returns_422(client: TestClient, field: str) -> None:
    payload = {key: value for key, value in PATIENT.items() if key != field}

    response = client.post("/patients", json=payload)

    assert response.status_code == 422


def test_create_patient_with_duplicate_email_returns_409(client: TestClient) -> None:
    client.post("/patients", json=PATIENT)

    response = client.post("/patients", json={**PATIENT, "name": "Martin"})

    assert response.status_code == 409
    assert response.json() == {"detail": "Email already registered"}


def test_list_patients(client: TestClient) -> None:
    client.post("/patients", json=PATIENT)
    client.post("/patients", json={**PATIENT, "name": "Martin", "email": "martin@example.com"})

    response = client.get("/patients")

    assert response.status_code == 200
    assert [patient["name"] for patient in response.json()] == ["Dupont", "Martin"]


def test_get_unknown_patient_returns_404(client: TestClient) -> None:
    response = client.get("/patients/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Patient not found"}
