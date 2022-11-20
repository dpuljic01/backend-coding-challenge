from fastapi import Query
from pydantic import BaseModel

from config import settings


class Pagination(BaseModel):
    page: int
    page_size: int

    @property
    def offset(self):
        return (self.page - 1) * self.page_size


def get_pagination_model(
    page: int = Query(default=1, gt=0),
    page_size: int = Query(default=settings.PAGE_SIZE, gt=0),
) -> Pagination:
    return Pagination(page=page, page_size=page_size)
