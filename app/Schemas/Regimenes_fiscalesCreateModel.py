from datetime import date
from pydantic import BaseModel, EmailStr

class Regimenes_fiscalesCreateRequestModel(BaseModel):
    codigo:str
    nombre:str
    descripcion:str
    
class Regimenes_fiscalesResponseModel(Regimenes_fiscalesCreateRequestModel):
    id:int

    
    