from datetime import date
from pydantic import BaseModel, EmailStr

class AgenteUpdateRequestModel(BaseModel):
    correo:str
    contrasena:str
    id:int

class AgenteUpdateResponseModel(AgenteUpdateRequestModel):
    id:int