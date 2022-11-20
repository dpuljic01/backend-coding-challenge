from typing import List

from sqlalchemy.orm import Session

from service.common.schemas import (
    PlanningModel,
    PlanningCreate,
    ClientModel,
    JobManagerModel,
    TalentModel,
    OfficeModel,
)
from service.database.models import Planning, Client, Talent, Office, JobManager
from service.database.session import Base, engine
from service.repositories import (
    PlanningRepository,
    ClientRepository,
    JobManagerRepository,
    TalentRepository,
    OfficeRepository,
)
from service.utils import process_datetime

tables = [Planning, Client, Talent, Office, JobManager]


async def init_database(session: Session, records: List[dict]) -> None:
    """Initialize DB and seed tables with records from plannings.json"""
    for table in tables:
        table.__table__.drop(bind=engine, checkfirst=True)

    Base.metadata.create_all(bind=engine)

    for record in records:
        process_datetime(record)
        original_record = PlanningModel(**record)

        if original_record.client_id:
            client_model = ClientModel(
                id=original_record.client_id,
                name=original_record.client_name,
            )
            await ClientRepository.get_or_create(
                session=session, model=Client, **client_model.dict()
            )

        if original_record.job_manager_id:
            job_manager_model = JobManagerModel(
                id=original_record.job_manager_id,
                name=original_record.job_manager_name,
            )
            await JobManagerRepository.get_or_create(
                session=session, model=JobManager, **job_manager_model.dict()
            )

        if original_record.talent_id:
            talent_model = TalentModel(
                id=original_record.talent_id,
                name=original_record.talent_name,
                grade=original_record.talent_grade,
            )
            await TalentRepository.get_or_create(
                session=session, model=Talent, **talent_model.dict()
            )

        office_model = OfficeModel(
            postal_code=original_record.office_postal_code,
            city=original_record.office_city,
        )
        await OfficeRepository.get_or_create(
            session=session, model=Office, **office_model.dict()
        )

        planning_model = PlanningCreate(**original_record.dict())
        await PlanningRepository.get_or_create(
            session=session, model=Planning, **planning_model.dict()
        )
