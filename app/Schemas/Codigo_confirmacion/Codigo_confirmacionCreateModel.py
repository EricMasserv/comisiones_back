from datetime import date
from pydantic import BaseModel, EmailStr

class Codigo_confirmacionCreateRequestModel(BaseModel):
    correo_agente:str
    codigo:str
    activo:int
    ip:str
    
class Codigo_confirmacionCreateResponseModel(Codigo_confirmacionCreateRequestModel):
    id:int

        