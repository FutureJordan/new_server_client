from fastapi import FastAPI
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Logins"

    id: Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[int] 

class Medecine(Base):
    __tablename__ = "Lecarstva"

    id: Mapped[int]= mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] 

engine = create_engine("sqlite:///Dadabase.db", echo=True)


Base.metadata.create_all(engine)