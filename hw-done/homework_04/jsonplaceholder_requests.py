"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio, aiohttp

import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_users_data() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            data: dict = await resp.json()
            return data


async def get_posts_data() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            data: dict = await resp.json()
            return data
