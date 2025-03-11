from pydantic import BaseModel

class PedidoCreate(BaseModel):
    user_id: int

    class Config:
        orm_mode = True

class PedidoResponse(BaseModel):
    id: int
    status: str
    user_id: int

    class Config:
        orm_mode = True
 
class UserCreate(BaseModel):
    username: str
    password: str        
