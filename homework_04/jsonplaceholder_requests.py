"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio, aiohttp, json
from dataclasses import dataclass

import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@dataclass
class Services:
    name: str
    url: str


@dataclass
class UsersData(Services):
    field_name: str
    field_username: str
    field_email: str


@dataclass
class PostsData(Services):
    field_user_id: int
    field_title: str
    field_body: str


USERS_DATA_URL = [
    UsersData(
        name="users",
        url="https://jsonplaceholder.typicode.com/users",
        field_name="name",
        field_username="username",
        field_email="email",
    ),
    PostsData(
        name="posts",
        url="https://jsonplaceholder.typicode.com/posts",
        field_user_id="userId",
        field_title="title",
        field_body="body",
    ),
]


async def fetch_json(service: Services) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            data: dict = await resp.json()
            return (data, service.name)


async def get_data() -> dict:
    data = {"users": {}, "posts": {}}
    tasks = {asyncio.create_task(fetch_json(url)) for url in USERS_DATA_URL}
    coro = asyncio.wait(tasks)
    done, __ = await coro
    for task in done:
        data_dict = task.result()
        if data_dict[-1] == "users":
            data["users"] = data_dict[0]
        elif data_dict[-1] == "posts":
            data["posts"] = data_dict[0]
    return data
