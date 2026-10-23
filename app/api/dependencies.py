from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.doctors import DoctorRepository
from app.repositories.patients import PatientRepository


def get_doctor_repository(db: Annotated[Session, Depends(get_db)]) -> DoctorRepository:
    return DoctorRepository(db)


def get_patient_repository(db: Annotated[Session, Depends(get_db)]) -> PatientRepository:
    return PatientRepository(db)


DoctorRepositoryDep = Annotated[DoctorRepository, Depends(get_doctor_repository)]
PatientRepositoryDep = Annotated[PatientRepository, Depends(get_patient_repository)]
