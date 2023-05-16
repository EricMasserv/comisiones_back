from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Validador import Validador
from ..Schemas.ValidadorCreateModel import ValidadorCreateRequestModel, ValidadorResponseModel
from ..Schemas.ValidadorUpdateModel import ValidadorUpdateRequestModel, ValidadorUpdateResponseModel

validador_router = APIRouter(
    prefix = "/validador",
    tags = ["Validador"]
)

@validador_router.post('/create')
async def create_validador(validador_request: ValidadorCreateRequestModel):
    validador = Validador.create(
        nombre_completo=validador_request.nombre_completo,
        correo=validador_request.correo,
        contraseña=validador_request.contraseña,
        estatus=validador_request.estatus
    )
    
    return validador_request

@validador_router.get('/show/{validador_id}')
async def get_validador(validador_id):
    validador = Validador.select().where(Validador.id == validador_id).first()
    if  validador:
        return ValidadorResponseModel(id=validador.id,
                                   nombre_completo=validador.nombre_completo,
                                   correo=validador.correo,
                                   contraseña=validador.contraseña,
                                   estatus=validador.estatus
                                 )
    else:
        return HTTPException(404, 'Validador no encontrada')
    
@validador_router.get('/delete/{validador_id}')
async def delete_validador(validador_id):
    validador = Validador.select().where(Validador.id == validador_id).first()
    if  validador:
        validador.delete_instance()
        return {'Validador eliminado'}
    else:
        return HTTPException(404, 'Validador not found')
    
@validador_router.post('/update/')
async def update_validador(validador_request: ValidadorUpdateRequestModel):
    validador = Validador.select().where(Validador.id == Validador.id).first()
    if validador:     
               
        qry=Validador.update({Validador.nombre_completo:validador_request.nombre_completo,
                              Validador.correo:validador_request.correo,
                              Validador.contraseña:validador_request.contraseña,
                              Validador.estatus:validador_request.estatus
                             }).where(Validador.id == validador_request.id)
        qry.execute()
                   
        return {'Validador actualizado'}
    else:
        return HTTPException(404, 'Validador no encontrado')