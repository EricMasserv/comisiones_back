from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Codigo_confirmacion import Codigo_confirmacion
from ..Schemas.Codigo_confirmacion.Codigo_confirmacionCreateModel import Codigo_confirmacionCreateRequestModel, Codigo_confirmacionCreateResponseModel
from ..Schemas.Codigo_confirmacion.Codigo_confirmacionUpdateModel import Codigo_confirmacionUpdateRequestModel, Codigo_confirmacionUpdateResponseModel
from ..Middlewares.verify_token_route import VerifyTokenRoute

codigo_confirmacion = APIRouter(
    prefix = "/codigo_confirmacion",
    tags = ["Codigo_confirmacion"],
    route_class=VerifyTokenRoute
)

@codigo_confirmacion.post('/create')
async def create_codigo_confirmacion(codigo_confirmacion_request: Codigo_confirmacionCreateRequestModel):
    codigo_confirmacion = Codigo_confirmacion.create(
        correo_agente=codigo_confirmacion_request.correo_agente,
        codigo=codigo_confirmacion_request.codigo,        
        activo=codigo_confirmacion_request.activo,        
        ip=codigo_confirmacion_request.ip,        
    )
    
    return codigo_confirmacion_request

@codigo_confirmacion.get('/show/{codigo_confirmacion_id}')
async def get_codigo_confirmacion(codigo_confirmacion_id):
    codigo_confirmacion = Codigo_confirmacion.select().where(Codigo_confirmacion.id == codigo_confirmacion_id).first()
    if  codigo_confirmacion:
        return Codigo_confirmacionCreateResponseModel(id=codigo_confirmacion.id,
                                    correo_agente = codigo_confirmacion.correo_agente,
                                    codigo = codigo_confirmacion.codigo,
                                    activo = codigo_confirmacion.activo,
                                    ip = codigo_confirmacion.ip,
                                )
    else:
        return HTTPException(404, 'Codigo de confirmacion no encontrado')
    
@codigo_confirmacion.get('/delete/{codigo_confirmacion_id}')
async def delete_codigo_confirmacion(codigo_confirmacion_id):
    codigo_confirmacion = Codigo_confirmacion.select().where(Codigo_confirmacion.id == codigo_confirmacion_id).first()
    if  codigo_confirmacion:
        codigo_confirmacion.delete_instance()
        return {'Codigo de confirmacion eliminado'}
    else:
        return HTTPException(404, 'Codigo de confirmacion no encontrado')
    
@codigo_confirmacion.post('/update/')
async def update_codigo_confirmacion(codigo_confirmacion_request: Codigo_confirmacionUpdateRequestModel):
    codigo_confirmacion = Codigo_confirmacion.select().where(Codigo_confirmacion.id == codigo_confirmacion_request.id).first()
    if codigo_confirmacion:     
               
        qry=codigo_confirmacion.update({Codigo_confirmacion.correo_agente : codigo_confirmacion_request.correo_agente,
                        Codigo_confirmacion.codigo : codigo_confirmacion_request.codigo,
                        Codigo_confirmacion.activo : codigo_confirmacion_request.activo,
                        Codigo_confirmacion.ip : codigo_confirmacion_request.ip,
                        }).where(Codigo_confirmacion.id == codigo_confirmacion_request.id)
        qry.execute()
                   
        return {'Centro de costo actualizado'}
    else:
        return HTTPException(404, 'Centro de costo no encontrao')