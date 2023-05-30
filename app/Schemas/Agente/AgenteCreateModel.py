from datetime import date
from pydantic import BaseModel, EmailStr

class AgenteCreateRequestModel(BaseModel):
    correo:str
    contrasena:str
        
class AgenteResponseModel(AgenteCreateRequestModel):
    id:int

    
    