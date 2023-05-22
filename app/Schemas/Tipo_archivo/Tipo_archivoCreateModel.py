from datetime import date
from pydantic import BaseModel, EmailStr

class TipoArchivoCreateRequestModel(BaseModel):
    nombre:str
    descripcion:str
    
class TipoArchivoResponseModel(TipoArchivoCreateRequestModel):
    id:int

    
    