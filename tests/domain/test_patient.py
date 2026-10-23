from datetime import date, timedelta

import pytest
from pydantic import ValidationError

from app.domain.patient import Patient


def make_patient(**overrides: object) -> Patient:
    data: dict[str, object] = {
        "id": 1,
        "name": "Dupont",
        "middlename": "Jean",
        "birthday": date(1990, 5, 17),
        "email": "jean.dupont@example.com",
    }
    data.update(overrides)
    return Patient.model_validate(data)


def test_create_patient() -> None:
    patient = make_patient()

    assert patient.email == "jean.dupont@example.com"


def test_birthday_today_is_accepted() -> None:
    patient = make_patient(birthday=date.today())

    assert patient.birthday == date.today()


def test_birthday_in_future_is_rejected() -> None:
    with pytest.raises(ValidationError, match="birthday cannot be in the future"):
        make_patient(birthday=date.today() + timedelta(days=1))


def test_invalid_email_is_rejected() -> None:
    with pytest.raises(ValidationError):
        make_patient(email="not-an-email")
