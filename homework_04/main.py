"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio, json
import asyncpg
from models import create_table, create_user, create_post
from jsonplaceholder_requests import get_users_data, get_posts_data



async def async_main():
    users_data, posts_data = await asyncio.gather(
        get_users_data(),
        get_posts_data(),
    )
    for users in users_data:
        await create_user(username=users['username'], name=users['name'], email=users['email'])
    for posts in posts_data:
        await create_post(user_id=posts['userId'], title=posts['title'], body=posts['body'])

def main():
    # create_table()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
