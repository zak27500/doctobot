from datetime import date

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base
from app.domain.doctor import Specialty


class DoctorModel(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    middlename: Mapped[str] = mapped_column(String(100))
    specialty: Mapped[Specialty] = mapped_column(
        # Stocke la valeur ("surgeon") plutôt que le nom du membre ("SURGEON")
        Enum(Specialty, native_enum=False, values_callable=lambda e: [m.value for m in e]),
        index=True,
    )


class PatientModel(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    middlename: Mapped[str] = mapped_column(String(100))
    birthday: Mapped[date]
    email: Mapped[str] = mapped_column(String(255), unique=True)
