from datetime import date

from sqlalchemy.orm import Session

from app.domain.doctor import DoctorCreate, Specialty
from app.domain.patient import PatientCreate
from app.repositories.doctors import DoctorRepository
from app.repositories.patients import PatientRepository


def test_doctor_repository_add_and_get(session: Session) -> None:
    repository = DoctorRepository(session)

    created = repository.add(
        DoctorCreate(name="Yang", middlename="Cristina", specialty=Specialty.SURGEON)
    )

    assert created.id == 1
    assert repository.get(created.id) == created
    assert repository.list_all() == [created]


def test_doctor_repository_get_unknown_returns_none(session: Session) -> None:
    assert DoctorRepository(session).get(999) is None


def test_patient_repository_add_and_get(session: Session) -> None:
    repository = PatientRepository(session)

    created = repository.add(
        PatientCreate(
            name="Dupont",
            middlename="Jean",
            birthday=date(1990, 5, 17),
            email="jean.dupont@example.com",
        )
    )

    assert created.id == 1
    assert repository.get(created.id) == created
    assert repository.get_by_email("jean.dupont@example.com") == created
    assert repository.list_all() == [created]


def test_patient_repository_get_by_unknown_email_returns_none(session: Session) -> None:
    assert PatientRepository(session).get_by_email("nobody@example.com") is None
