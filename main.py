import asyncio

import asyncpg
from aiohttp import web

from view import hello, read_file_request, write_file_request, store_image_handler, get_image_handler


async def init_app():
    app = web.Application()

    app["pool"] = await asyncpg.create_pool(
        host="localhost", port="5432", database="postgres", user="postgres", password="qwerty"
    )

    app.add_routes([web.get("/", hello), web.get("/{filename}", read_file_request), web.post("/", write_file_request),
                    web.post('/image', store_image_handler), web.get('/image/{filename}', get_image_handler)])
    return app


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    web.run_app(app, loop=loop)
