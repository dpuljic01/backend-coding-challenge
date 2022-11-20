import datetime
from typing import Optional, List

from pydantic import BaseModel

from service.utils import to_camel_case


class SkillModel(BaseModel):
    name: str
    category: str


class OfficeModel(BaseModel):
    postal_code: str
    id: Optional[int]
    city: Optional[str]


class TalentModel(BaseModel):
    id: Optional[str]
    name: Optional[str]
    grade: Optional[str]


class ClientModel(BaseModel):
    id: str
    name: Optional[str]


class JobManagerModel(BaseModel):
    id: Optional[str]
    name: Optional[str]


class PlanningModel(BaseModel):
    id: int
    original_id: str
    client_id: str
    operating_unit: str
    total_hours: float
    is_unassigned: bool
    start_date: datetime.datetime
    end_date: datetime.datetime
    required_skills: List[SkillModel]
    optional_skills: List[SkillModel]

    job_manager_id: Optional[str]
    job_manager_name: Optional[str]
    client_name: Optional[str]
    talent_id: Optional[str]
    talent_name: Optional[str]
    talent_grade: Optional[str]
    office_city: Optional[str]
    office_postal_code: Optional[str]
    booking_grade: Optional[str]
    industry: Optional[str]

    class Config:
        alias_generator = to_camel_case


class PlanningCreate(BaseModel):
    id: int
    original_id: str
    client_id: str
    talent_id: str
    job_manager_id: str
    operating_unit: str
    total_hours: float
    is_unassigned: bool
    required_skills: List[SkillModel]
    optional_skills: List[SkillModel]
    start_date: datetime.datetime
    end_date: datetime.datetime
    office_id: Optional[int]
    booking_grade: Optional[str]
    industry: Optional[str]
