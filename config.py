import os

from pydantic import BaseSettings

ROOT_DIR = os.path.abspath(os.curdir)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Planner"
    PAGE_SIZE: int = 100
    DATABASE_NAME: str = "planning.db"
    SQLALCHEMY_DATABASE_URL: str = f"sqlite:///{DATABASE_NAME}"


settings = Settings()
