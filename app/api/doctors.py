from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import DoctorRepositoryDep
from app.domain.doctor import Doctor, DoctorCreate

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.post("", status_code=status.HTTP_201_CREATED, summary="Register a robot doctor")
def create_doctor(payload: DoctorCreate, repository: DoctorRepositoryDep) -> Doctor:
    return repository.add(payload)


@router.get("", summary="List doctors")
def list_doctors(repository: DoctorRepositoryDep) -> list[Doctor]:
    return repository.list_all()


@router.get(
    "/{doctor_id}",
    summary="Get a doctor",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Doctor not found"}},
)
def get_doctor(doctor_id: int, repository: DoctorRepositoryDep) -> Doctor:
    doctor = repository.get(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    return doctor
