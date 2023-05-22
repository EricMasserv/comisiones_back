from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Validador import Validador
from ..Models.Usuario import Usuario
from passlib.context import CryptContext
from ..Schemas.Validador.ValidadorCreateModel import ValidadorCreateRequestModel, ValidadorResponseModel
from ..Schemas.Validador.ValidadorUpdateModel import ValidadorUpdateRequestModel, ValidadorUpdateResponseModel
from ..Middlewares.verify_token_route import VerifyTokenRoute

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

validador_router = APIRouter(
    prefix = "/validador",
    tags = ["Validador"],
    route_class=VerifyTokenRoute
)

@validador_router.post('/create')
async def create_validador(validador_request: ValidadorCreateRequestModel):
    usuario = Usuario.create(
        correo=validador_request.correo,
        contrasena=pwd_context.hash(validador_request.contrasena),
        tipo='validador'        
    )
    
    id_usuario = Usuario.select(Usuario.id).where(Usuario.correo == validador_request.correo).dicts()[0]
    
    validador = Validador.create(
        nombre_completo=validador_request.nombre_completo,
        correo=validador_request.correo,
        contrasena=pwd_context.hash(validador_request.contrasena),
        estatus=validador_request.estatus,
        id_usuario=id_usuario['id']
    )
    
    return validador_request

@validador_router.get('/show/{validador_id}')
async def get_validador(validador_id):
    validador = Validador.select().where(Validador.id == validador_id).first()
    if  validador:
        return ValidadorResponseModel(id=validador.id,
                                   nombre_completo=validador.nombre_completo,
                                   correo=validador.correo,
                                   contrasena=validador.contrasena,
                                   estatus=validador.estatus
                                 )
    else:
        return HTTPException(404, 'Validador no encontrada')
    
@validador_router.get('/delete/{validador_id}')
async def delete_validador(validador_id):
    validador = Validador.select().where(Validador.id == validador_id).first()
    usuario = Usuario.select().where(Usuario.correo == validador.correo).first()
    if  validador:
        validador.delete_instance()
        usuario.delete_instance()
        return {'Validador eliminado'}
    else:
        return HTTPException(404, 'Validador not found')
    
@validador_router.post('/update/')
async def update_validador(validador_request: ValidadorUpdateRequestModel):
    validador = Validador.select(Validador.correo).where(Validador.id == validador_request.id).dicts()[0]
    if validador:         
        qry=Validador.update({Validador.nombre_completo:validador_request.nombre_completo,
                              Validador.correo:validador_request.correo,
                              Validador.contrasena:pwd_context.hash(validador_request.contrasena),
                              Validador.estatus:validador_request.estatus
                             }).where(Validador.id == validador_request.id)
        qry.execute()
        qryUser=Usuario.update({Usuario.correo:validador_request.correo,
                                Usuario.contrasena:pwd_context.hash(validador_request.contrasena),
                             }).where(Usuario.correo == validador['correo'])
        qryUser.execute()
                   
        return {'Validador actualizado'}
    else:
        return HTTPException(404, 'Validador no encontrado')