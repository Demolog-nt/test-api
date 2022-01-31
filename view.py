from aiohttp import web

from controller import text_from_database, text_to_database, image_from_database, image_to_database
from schemas import *


async def hello(request):
    return web.Response(text="Hello")


async def read_file_request(request):
    status, message, html_status = await text_from_database(request)
    response = GetResponse().load({"status": status, "message": message})
    return web.json_response(response, status=html_status)


async def write_file_request(request):
    file_to_write = await request.json()
    status, message, html_status = await text_to_database(request, file_to_write)
    response = PostResponse().load({"status": status, "message": message})
    return web.json_response(response, status=html_status)


async def store_image_handler(request):

    reader = await request.multipart()

    field = await reader.next()
    assert field.name == 'file'
    filename = field.filename
    write_content = await field.read()
    status, message, html_status = await image_to_database(request, filename, write_content)

    response = PostResponse().load({"status": status, "message": message})
    return web.json_response(response, status=html_status)


async def get_image_handler(request):
    status, message, html_status, image = await image_from_database(request)
    response = GetResponse().load({"status": status, "message": message})
    return web.json_response(response, status=html_status)