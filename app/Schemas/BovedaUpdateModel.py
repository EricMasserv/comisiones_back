from datetime import date
from pydantic import BaseModel, EmailStr

class BovedaUpdateRequestModel(BaseModel):
    nombre:str
    valor:str
    descripcion:str
    id:int

class BovedaUpdateResponseModel(BovedaUpdateRequestModel):
    id:int