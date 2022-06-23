from .database import db
from sqlalchemy import Column, String, Integer, Boolean


class Product(db.Model):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String(500))

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
