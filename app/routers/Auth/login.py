from fastapi import APIRouter
from passlib.context import CryptContext
from ...Models.Usuario import Usuario
from fastapi.security import OAuth2PasswordBearer
from ...Schemas.Login.LoginRequest import UsuarioLoginRequest, UsuarioLoginResponse
from datetime import datetime, timedelta
from jose import jwt
from ...Config.config_env import *

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

login = APIRouter(
    prefix = "/login",
    tags = ["Login"]
)

oauth2_scheme = OAuth2PasswordBearer("/token")

async def create_token(data:dict, expires_delta: timedelta = None):
    data_copy = data.copy()
    if expires_delta is None:
        expire = datetime.utcnow() + timedelta(minutes=15)
    else:
        expire = datetime.utcnow() + expires_delta
    data_copy.update({"exp": expire})
    encoded_jwt = jwt.encode(data_copy, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt

@login.post('/iniciar_sesion')
async def iniciar_sesion(login_request: UsuarioLoginRequest):
    usuario= False
    try:      
        usuario = Usuario.select().where(Usuario.correo == login_request.correo).dicts()[0]
    except:
        print("Las credenciales no coinciden")

    dict_usuario = Usuario.select().where(Usuario.correo == login_request.correo).first()
    
    
    if usuario:
        if pwd_context.verify(login_request.contrasena, usuario['contrasena']):
            
          datos = UsuarioLoginResponse(id=usuario['id'],
                                    correo = usuario['correo'],
                                    contrasena = usuario['contrasena'],
                                    tipo = usuario['tipo'],
                                )
          
          token_expiracion = timedelta(minutes=30)
          access_token = await create_token({"sub": dict_usuario.correo}, token_expiracion)
                    
          return {
            "datos": datos,
            "acceso": True,
            "perfil":usuario['tipo'],
            "access_token": access_token,
            "token_type": "bearer"
        }
          
        else:
          return 'Las credenciales no coinciden'  
    else:
        return 'Las credenciales no coinciden' 