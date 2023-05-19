from datetime import date
from pydantic import BaseModel, EmailStr

class ValidadorUpdateRequestModel(BaseModel):
    nombre_completo:str
    correo:str
    contrasena:str
    estatus:int
    
    id:int

class ValidadorUpdateResponseModel(ValidadorUpdateRequestModel):
    id:int