import asyncio
from aiohttp import web
from app.routes import routes
from app.db import connect


async def init():
    app = web.Application()
    app.add_routes(routes)
    app["db"] = await connect()

    return app


def main():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init())
    web.run_app(app)
