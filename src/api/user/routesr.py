from fastapi import FastAPI
from fastapi import HTTPException



from src.api.Database import Medecine
from src.api.Database import engine

from src.api.Database import User
from src.api.medicine.models import Get_medecine
from src.api.medicine.models import lst_med
from models import Login_user

from sqlalchemy.orm import Session
from sqlalchemy import select


app = FastAPI()

@app.post("/registraciya")
async def create(user: Login_user):
    with Session(engine) as session:
        users = User(
            name = user.name,
            password = user.password
        )
        session.add(users)
        session.commit()


@app.get("/login")
async def logins(name: str, password: int):
    with Session(engine) as session:
        stmt = select(User).where(User.name == name, User.password == password)
        user = session.scalar(stmt)
        if not user:
            raise HTTPException(status_code=404, detail="Не найдено!")
        return user


@app.post("/products")
async def product(product: Get_medecine):
    with Session(engine) as session:
        product = Medecine(
            title = product.title,
            price = product.price
        )
        session.add(product)
        session.commit()


@app.get("/product", response_model=lst_med)
async def prod_get():
    session = Session(engine)
    prod = select(Medecine)
    lst = session.scalars(prod)
    return {'lst': lst}
