import uvicorn
from fastapi import FastAPI

from config import settings
from service.api.v1.routers import api_router

application = FastAPI(title=settings.PROJECT_NAME)
application.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:application")
