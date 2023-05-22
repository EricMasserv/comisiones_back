from datetime import date
from pydantic import BaseModel, EmailStr

class Regimenes_fiscalesUpdateRequestModel(BaseModel):
    codigo:str
    nombre:str
    descripcion:str
    id:int

class Regimenes_fiscalesUpdateResponseModel(Regimenes_fiscalesUpdateRequestModel):
    id:int