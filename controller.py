import typing

from marshmallow import ValidationError
from typing import Tuple

from constants import InvalidData, Status
from schemas import Data
from utility import random_lower_string
from models.textdb import TextQueries
from models.imagedb import ImageQueries


async def text_to_database(request, data: dict) -> Tuple[str, str, int]:
    pool = request.app["pool"]
    try:
        Data().load(data)
    except ValidationError as error:
        return Status.ERROR.value, InvalidData.INVALID.value, 400

    filename = random_lower_string(10)
    async with pool.acquire() as connection:
        async with connection.transaction():
            await connection.execute(TextQueries.INSERT, filename, data)
    return Status.SUCCESS.value, filename, 200


async def text_from_database(request) -> Tuple[str, str, int]:
    pool = request.app["pool"]
    filename = request.match_info["filename"]
    async with pool.acquire() as connection:
        async with connection.transaction():
            file_to_read = await connection.fetchval(TextQueries.SELECT, filename)
    return Status.SUCCESS.value, file_to_read, 200


async def image_to_database(request, filename: str, data: bytearray) -> Tuple[str, str, int]:
    pool = request.app["pool"]

    async with pool.acquire() as connection:
        async with connection.transaction():
            await connection.execute(ImageQueries.INSERT, filename, data)
    return Status.SUCCESS.value, filename, 200


async def image_from_database(request) -> Tuple[str, str, int, typing.BinaryIO]:
    pool = request.app["pool"]
    filename = request.match_info["filename"]
    async with pool.acquire() as connection:
        async with connection.transaction():
            image_to_read = await connection.fetchval(ImageQueries.SELECT, filename)
    with open(f"{filename}.jpg", 'wb') as new_image:
        new_image.write(image_to_read)
    return Status.SUCCESS.value, filename, 200, new_image
