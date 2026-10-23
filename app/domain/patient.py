from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class PatientBase(BaseModel):
    name: str = Field(min_length=1)
    middlename: str = Field(min_length=1)
    birthday: date
    email: EmailStr

    @field_validator("birthday")
    @classmethod
    def birthday_not_in_future(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("birthday cannot be in the future")
        return value


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
