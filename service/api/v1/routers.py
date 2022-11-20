from fastapi import APIRouter

from service.api.v1.endpoints import plannings

api_router = APIRouter()
api_router.include_router(plannings.router, prefix="/plannings", tags=["plannings"])
