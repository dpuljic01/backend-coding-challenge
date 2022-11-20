from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Boolean,
    JSON,
    Float,
)
from sqlalchemy.orm import relationship

from service.database.session import Base


class Office(Base):
    __tablename__ = "offices"

    id = Column(Integer, primary_key=True)
    postal_code = Column(String(128), nullable=False)
    city = Column(String(128))

    plannings = relationship("Planning", backref="office")


class Talent(Base):
    __tablename__ = "talents"

    id = Column(String(256), primary_key=True)
    name = Column(String(256), index=True)
    grade = Column(String(256))

    plannings = relationship("Planning", backref="talent")


class Client(Base):
    __tablename__ = "clients"

    id = Column(String(256), primary_key=True)
    name = Column(String(256))

    plannings = relationship("Planning", backref="client")


class JobManager(Base):
    __tablename__ = "job_managers"

    id = Column(String(256), primary_key=True)
    name = Column(String(256))

    plannings = relationship("Planning", backref="job_manager")


class Planning(Base):
    __tablename__ = "plannings"

    id = Column(Integer, primary_key=True)
    original_id = Column(String(256), nullable=False, unique=True)
    operating_unit = Column(String(256), nullable=False)
    total_hours = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    booking_grade = Column(String(256))
    industry = Column(String(256))
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean, nullable=False, default=True)

    # ---- relationships ----
    client_id = Column(String(256), ForeignKey("clients.id"), index=True)
    office_id = Column(Integer, ForeignKey("offices.id"), index=True)
    talent_id = Column(String(256), ForeignKey("talents.id"), index=True)
    job_manager_id = Column(String(256), ForeignKey("job_managers.id"), index=True)
