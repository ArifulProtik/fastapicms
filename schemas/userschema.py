from pydantic import BaseModel

class Userbase(BaseModel):
    email: str
    name: str
    username: str
    

class UserCreate(Userbase):
    password: str


class Userinfo(Userbase):
    id: str
    class Config():
        orm_mode = True

class Userlogin(BaseModel):
    email:str
    password: str