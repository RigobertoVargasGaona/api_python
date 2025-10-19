from pydantic import BaseModel

class RolCreate(BaseModel):
    rol_name: str

class RolResponse(RolCreate):
    rol_id: int

    class Config:
        orm_mode = True