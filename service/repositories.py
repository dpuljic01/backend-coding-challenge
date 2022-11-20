from dataclasses import dataclass
from typing import List

from sqlalchemy.orm import Session, Query

from service.common import schemas
from service.common.filters import PlanningFilter
from service.common.order import Order, OrderPair
from service.common.pagination import Pagination
from service.database.models import Planning
from service.utils import apply_ordering, apply_pagination


@dataclass
class BaseRepository:
    @classmethod
    async def get_or_create(cls, session: Session, model, **obj_in):
        instance = session.query(model).filter_by(**obj_in).one_or_none()
        if instance:
            return instance

        instance = model(**obj_in)
        session.add(instance)
        session.flush()
        return instance


class PlanningRepository(BaseRepository):
    @staticmethod
    def _get_planning_query(
        session: Session,
        planning_filter: PlanningFilter,
        order: Order = None,
        pagination: Pagination = None,
    ) -> Query:
        query = session.query(Planning)
        if planning_filter.id:
            query = query.filter(Planning.id == planning_filter.id)
        if planning_filter.original_id:
            query = query.filter(Planning.original_id == planning_filter.original_id)

        if order:
            query = apply_ordering(query, order)
        if pagination:
            query = apply_pagination(query, pagination)

        return query

    @classmethod
    def list(
        cls,
        session: Session,
        planning_filter: PlanningFilter,
        order: Order = Order(pairs=[OrderPair(field="id")]),
        pagination: Pagination = None,
    ) -> List[schemas.PlanningModel]:
        query = cls._get_planning_query(session, planning_filter, order, pagination)
        return query.all()


class TalentRepository(BaseRepository):
    ...


class OfficeRepository(BaseRepository):
    ...


class ClientRepository(BaseRepository):
    ...


class JobManagerRepository(BaseRepository):
    ...
