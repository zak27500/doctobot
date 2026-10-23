from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import PatientRepositoryDep
from app.domain.patient import Patient, PatientCreate

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Register a patient",
    responses={status.HTTP_409_CONFLICT: {"description": "Email already registered"}},
)
def create_patient(payload: PatientCreate, repository: PatientRepositoryDep) -> Patient:
    if repository.get_by_email(payload.email) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    return repository.add(payload)


@router.get("", summary="List patients")
def list_patients(repository: PatientRepositoryDep) -> list[Patient]:
    return repository.list_all()


@router.get(
    "/{patient_id}",
    summary="Get a patient",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Patient not found"}},
)
def get_patient(patient_id: int, repository: PatientRepositoryDep) -> Patient:
    patient = repository.get(patient_id)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return patient
