"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os, asyncpg
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship,
)

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)


async_engine = create_async_engine(url=PG_CONN_URI)
Session: AsyncSession = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)


class Base:
    id = Column(Integer, primary_key=True)

    def __str__(self):
        return (
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r} "
        )

    def __repr__(self):
        return str(self)


Base = declarative_base(bind=async_engine, cls=Base)


class User(Base):
    __tablename__ = "User"
    name = Column("name", String)
    username = Column("username", String, unique=True)
    email = Column("email", String, unique=True)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "Post"
    user_id = Column("user_id", Integer, ForeignKey("User.id"))
    title = Column("title", String)
    body = Column("body", String)
    user = relationship("User", back_populates="posts")


async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(name: str, username: str, email: str) -> User:
    async with Session() as session:
        username = User(username=username, name=name, email=email)
        session.add(username)
        await session.commit()
        await session.refresh(username)
    return username


async def create_posts_for_user(user_id: int, title: str, body: str) -> Post:
    async with Session() as session:
        post = Post(user_id=user_id, title=title, body=body)
        session.add(post)
        await session.commit()
        await session.refresh(post)
    return post
