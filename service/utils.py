from datetime import datetime
from typing import TypeVar, Generic

from sqlalchemy import desc, asc
from sqlalchemy.orm import Query

from service.common.enums import OrderDirectionEnum
from service.common.order import Order
from service.common.pagination import Pagination

CustomModel = TypeVar("CustomModel")


def prepare_response(model: Generic[CustomModel], meta: dict = None):
    if not meta:
        meta = {"code": 200, "message": "ok"}
    return {"content": model, "meta": meta}


def process_datetime(record) -> dict:
    record["startDate"] = datetime.strptime(record["startDate"], "%m/%d/%Y %I:%M %p")
    record["endDate"] = datetime.strptime(record["endDate"], "%m/%d/%Y %I:%M %p")
    return record


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def apply_pagination(query: Query, pagination: Pagination) -> Query:
    query = query.limit(pagination.page_size)
    if pagination.offset:
        query = query.offset(pagination.offset)
    return query


def apply_ordering(query: Query, order: Order) -> Query:
    for order_pair in order.pairs:
        order_by_field = order_pair.field
        if order_pair.direction == OrderDirectionEnum.DESC:
            order_by_field = desc(order_by_field)
        else:
            order_by_field = asc(order_by_field)
        query = query.order_by(order_by_field)
    return query
