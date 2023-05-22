from datetime import date
from pydantic import BaseModel, EmailStr

class Centro_costoCreateRequestModel(BaseModel):
    nombre:str
    descripcion:str
    
class Centro_costoResponseModel(Centro_costoCreateRequestModel):
    id:int

    
    