from typing import List, Any

from fastapi import Query
from pydantic import BaseModel

from service.common.enums import OrderDirectionEnum


class OrderPair(BaseModel):
    field: Any  # This could be str as field name or an InstrumentedAttribute from sqlalchemy model
    direction: OrderDirectionEnum = OrderDirectionEnum.ASC


class Order(BaseModel):
    pairs: List[OrderPair]


def get_ordering(
    planning_id: OrderDirectionEnum = Query(
        default=None,
        description="Order plannings by ID",
        alias="planningID",
    ),
    original_id: OrderDirectionEnum = Query(
        default=None,
        description="Order plannings by originalID",
        alias="originalID",
    ),
) -> Order:
    order_pairs = []
    if planning_id:
        order_pairs.append(OrderPair(field="id", direction=planning_id))
    if original_id:
        order_pairs.append(OrderPair(field="original_id", direction=original_id))

    return Order(pairs=order_pairs)
