from fastapi import APIRouter
from fastapi import HTTPException
from passlib.context import CryptContext
from ..Models.Usuario import Usuario
from ..Schemas.UsuarioRegistrarModel import UsuarioRegistrarRequestModel, UsuarioResponseModel
from ..Schemas.UsuarioUpdateModel import UsuarioUpdateRequestModel, UsuarioUpdateResponseModel
from ..Schemas.UsuarioLoginRequest import UsuarioLoginRequest, UsuarioLoginResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

usuario = APIRouter(
    prefix = "/usuario",
    tags = ["Usuario"]
)

@usuario.post('/login')
async def login(login_request: UsuarioLoginRequest):
    usuario = Usuario.select().where(Usuario.correo == login_request.correo).dicts()[0]
    
    if usuario:
        if pwd_context.verify(login_request.contrasena, usuario['contrasena']):
            
          datos = UsuarioLoginResponse(id=usuario['id'],
                                    correo = usuario['correo'],
                                    contrasena = usuario['contrasena'],
                                    tipo = usuario['tipo'],
                                )
          return {
            "datos": datos,
            "acceso": True,
            "perfil":usuario['tipo']
        }
          
        else:
          return 'Las credenciales no coinciden'  
    else:
        return 'No existe' 
    
@usuario.post('/registrar')
async def registrar_usuario(usuario_request: UsuarioRegistrarRequestModel):
    usuario = Usuario.create(
        correo=usuario_request.correo,
        contrasena=pwd_context.hash(usuario_request.contrasena),
        tipo=usuario_request.tipo        
    )
    
    return usuario_request

@usuario.get('/show/{usuario_id}')
async def get_usuario(usuario_id):
    usuario = Usuario.select().where(Usuario.id == usuario_id).first()
    if  usuario:
        return UsuarioResponseModel(id=usuario.id,
                                    correo = usuario.correo,
                                    contrasena = usuario.contrasena,
                                    tipo = usuario.tipo,
                                )
    else:
        return HTTPException(404, 'Usuario no encontrado')
    
@usuario.get('/delete/{usuario_id}')
async def delete_usuario(usuario_id):
    usuario = Usuario.select().where(Usuario.id == usuario_id).first()
    if  usuario:
        usuario.delete_instance()
        return {'Usuario eliminado'}
    else:
        return HTTPException(404, 'Usuario no encontrado')
    
@usuario.post('/update/')
async def update_usuario(usuario_request: UsuarioUpdateRequestModel):
    usuario = Usuario.select().where(Usuario.id == usuario_request.id).first()
    if usuario:     
               
        qry=Usuario.update({Usuario.correo : usuario_request.correo,
                        Usuario.contrasena : pwd_context.hash(usuario_request.contrasena),
                        Usuario.tipo : usuario_request.tipo
                        }).where(Usuario.id == usuario_request.id)
        qry.execute()
                   
        return {'Usuario actualizado'}
    else:
        return HTTPException(404, 'Usuario no encontrado')