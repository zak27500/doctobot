from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import DoctorModel
from app.domain.doctor import Doctor, DoctorCreate


class DoctorRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, doctor: DoctorCreate) -> Doctor:
        row = DoctorModel(**doctor.model_dump())
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return Doctor.model_validate(row)

    def get(self, doctor_id: int) -> Doctor | None:
        row = self._session.get(DoctorModel, doctor_id)
        return Doctor.model_validate(row) if row else None

    def list_all(self) -> list[Doctor]:
        rows = self._session.scalars(select(DoctorModel).order_by(DoctorModel.id))
        return [Doctor.model_validate(row) for row in rows]
