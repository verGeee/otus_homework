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
from .models import create_table, create_user, create_post
from .jsonplaceholder_requests import get_data





async def async_main():
    ### Get data for uploading
    data: dict = await get_data()
    users_data: dict = data["users"]
    posts_data: dict = data["posts"]

    ### Push to DB
    # for users in users_data:
    #     create_user(username=users['username'], name=users['name'], email=users['email'])
    for posts in posts_data:
        await create_post(user_id=posts['userId'], title=posts['title'], body=posts['body'])




def main():
    create_table()

if __name__ == "__main__":
    # pass
    # main()
    asyncio.run(async_main())
