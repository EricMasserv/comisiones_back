from datetime import date
from pydantic import BaseModel, EmailStr

class ValidadorCreateRequestModel(BaseModel):
    nombre_completo:str
    correo:str
    contraseña:str
    estatus:int
    
class ValidadorResponseModel(ValidadorCreateRequestModel):
    id:int

    
    