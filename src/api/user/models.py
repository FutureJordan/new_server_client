from pydantic import BaseModel

class Login_user(BaseModel):
    id: int  
    name: str
    password: int



class Out_user(BaseModel):
    id: int  
    name: str
    password: int