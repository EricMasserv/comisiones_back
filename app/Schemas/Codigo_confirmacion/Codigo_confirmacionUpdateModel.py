from datetime import date
from pydantic import BaseModel, EmailStr

class Codigo_confirmacionUpdateRequestModel(BaseModel):
    correo_agente:str
    codigo:str
    activo:int
    ip:str
    id:int

class Codigo_confirmacionUpdateResponseModel(Codigo_confirmacionUpdateRequestModel):
    id:int