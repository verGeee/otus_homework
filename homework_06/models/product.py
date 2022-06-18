from .database import db
from sqlalchemy import Column, String, Integer, Boolean


class Product(db.Model):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
