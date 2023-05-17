from datetime import date
from pydantic import BaseModel, EmailStr

class BovedaCreateRequestModel(BaseModel):
    nombre:str
    valor:str
    descripcion:str
    
class BovedaResponseModel(BovedaCreateRequestModel):
    id:int

    
    