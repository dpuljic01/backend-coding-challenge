from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.common.filters import PlanningFilter, get_planning_filter
from service.common.order import Order, get_ordering
from service.common.pagination import Pagination, get_pagination_model
from service.database.session import get_database
from service.repositories import PlanningRepository
from service.utils import prepare_response

router = APIRouter()


@router.get("")
async def list_plannings(
    pagination: Pagination = Depends(get_pagination_model),
    filter_: PlanningFilter = Depends(get_planning_filter),
    order: Order = Depends(get_ordering),
    db: Session = Depends(get_database),
):
    plannings = PlanningRepository.list(
        session=db,
        planning_filter=filter_,
        order=order,
        pagination=pagination,
    )

    return prepare_response(plannings)
