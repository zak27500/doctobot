import pytest
from pydantic import ValidationError

from app.domain.doctor import Doctor, Specialty


def test_create_doctor() -> None:
    doctor = Doctor(id=1, name="House", middlename="Gregory", specialty=Specialty.GENERAL)

    assert doctor.specialty is Specialty.GENERAL


def test_specialty_accepts_string_value() -> None:
    doctor = Doctor.model_validate(
        {"id": 1, "name": "Yang", "middlename": "Cristina", "specialty": "surgeon"}
    )

    assert doctor.specialty is Specialty.SURGEON


def test_unknown_specialty_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Doctor.model_validate(
            {"id": 1, "name": "Doe", "middlename": "John", "specialty": "dentist"}
        )


def test_empty_name_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Doctor(id=1, name="", middlename="John", specialty=Specialty.OPTICIAN)
