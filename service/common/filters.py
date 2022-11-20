from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel, PositiveInt


class ClientFilter(BaseModel):
    id: Optional[List[str]]
    name: Optional[str]


class TalentFilter(BaseModel):
    id: Optional[List[str]]
    name: Optional[str]
    category: Optional[str]


class PlanningFilter(BaseModel):
    id: Optional[int] = None
    original_id: Optional[str] = None
    client_id: Optional[ClientFilter] = None
    ...  # etc


def get_planning_filter(
    planning_id: Optional[PositiveInt] = Query(
        default=None, description="Filter by planningID"
    ),
    original_id: Optional[str] = Query(
        default=None, description="Filter by originalID"
    ),
    client_id: Optional[PositiveInt] = Query(
        default=None, description="Filter by clientID"
    ),
) -> Optional[PlanningFilter]:
    planning_filter = PlanningFilter(
        id=planning_id,
        client_id=client_id,
        original_id=original_id,
    )
    return planning_filter
