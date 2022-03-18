from bot_api.settings.base import *
from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['bot_api.database.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

