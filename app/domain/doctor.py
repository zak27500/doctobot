from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Specialty(StrEnum):
    GENERAL = "general"
    SURGEON = "surgeon"
    OPTICIAN = "optician"


class DoctorBase(BaseModel):
    name: str = Field(min_length=1)
    middlename: str = Field(min_length=1)
    specialty: Specialty


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
