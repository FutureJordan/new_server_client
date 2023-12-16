from pydantic import BaseModel

class Get_medecine(BaseModel):
    id: int
    title: str
    price: int


class Out_medecine(BaseModel):
    id: int
    title: str
    price: int


class lst_med(BaseModel):
    lst: list[Out_medecine]