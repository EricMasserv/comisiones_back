from datetime import date
from pydantic import BaseModel, EmailStr

class UsuarioUpdateRequestModel(BaseModel):
    correo:str
    nombre_usuario:str
    contrasena:str
    tipo:str  
    id:int

class UsuarioUpdateResponseModel(UsuarioUpdateRequestModel):
    id:int