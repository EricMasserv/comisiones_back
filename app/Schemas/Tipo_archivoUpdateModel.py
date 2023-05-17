from datetime import date
from pydantic import BaseModel, EmailStr

class TipoArchivoUpdateRequestModel(BaseModel):
    nombre:str
    descripcion:str
    id:int

class TipoArchivoUpdateResponseModel(TipoArchivoUpdateRequestModel):
    id:int