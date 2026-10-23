from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import PatientModel
from app.domain.patient import Patient, PatientCreate


class PatientRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, patient: PatientCreate) -> Patient:
        row = PatientModel(**patient.model_dump())
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return Patient.model_validate(row)

    def get(self, patient_id: int) -> Patient | None:
        row = self._session.get(PatientModel, patient_id)
        return Patient.model_validate(row) if row else None

    def get_by_email(self, email: str) -> Patient | None:
        row = self._session.scalar(select(PatientModel).where(PatientModel.email == email))
        return Patient.model_validate(row) if row else None

    def list_all(self) -> list[Patient]:
        rows = self._session.scalars(select(PatientModel).order_by(PatientModel.id))
        return [Patient.model_validate(row) for row in rows]
