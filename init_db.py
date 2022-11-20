import asyncio
import json
import logging
import os.path
from pathlib import Path

import click

from service.database.db import init_database
from service.database.session import SessionLocal

logger = logging.getLogger(__name__)


async def init_db() -> None:
    click.echo("Started DB initialization..")
    filename = Path(__file__).parent / "planning.json"
    if not os.path.isfile(filename):
        click.echo(f"Missing file {filename}")
        return

    session = SessionLocal()
    with open(filename) as plannings:
        await init_database(session=session, records=json.load(plannings))
    session.commit()
    session.close()
    click.echo("Finished DB initialization")


if __name__ == "__main__":
    asyncio.run(init_db())
