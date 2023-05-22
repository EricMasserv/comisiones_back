from datetime import date
from pydantic import BaseModel, EmailStr

class UsuarioLoginRequest(BaseModel):
    correo:str
    contrasena:str  
    
class UsuarioLoginResponse(UsuarioLoginRequest):
    id:int

    
    