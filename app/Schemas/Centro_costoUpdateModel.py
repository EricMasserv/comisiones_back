from datetime import date
from pydantic import BaseModel, EmailStr

class Centro_costoUpdateRequestModel(BaseModel):
    nombre:str
    descripcion:str
    id:int

class Centro_costoUpdateResponseModel(Centro_costoUpdateRequestModel):
    id:int