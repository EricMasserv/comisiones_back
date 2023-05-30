from datetime import date
from pydantic import BaseModel, EmailStr

class UsuarioRegistrarRequestModel(BaseModel):
    correo:str
    nombre_usuario:str
    contrasena:str
    tipo:str
    
class UsuarioResponseModel(UsuarioRegistrarRequestModel):
    id:int

    
    