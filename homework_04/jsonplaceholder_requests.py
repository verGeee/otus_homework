"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio, aiohttp, json

import platform

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/1"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_user_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            return await resp.json()


async def post_user_data():
    async with aiohttp.ClientSession() as session:
        async with session.post(POSTS_DATA_URL) as resp:
            return await resp.json()


if __name__ == "__main__":
    pass
