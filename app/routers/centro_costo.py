from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Centro_costo import Centro_costo
from ..Schemas.Centro_costo.Centro_costoCreateModel import Centro_costoCreateRequestModel, Centro_costoResponseModel
from ..Schemas.Centro_costo.Centro_costoUpdateModel import Centro_costoUpdateRequestModel, Centro_costoUpdateResponseModel
from ..Middlewares.verify_token_route import VerifyTokenRoute

centro_costo = APIRouter(
    prefix = "/centro_costo",
    tags = ["Centro_costo"],
    route_class=VerifyTokenRoute
)

@centro_costo.post('/create')
async def create_centro_costo(centro_costo_request: Centro_costoCreateRequestModel):
    centro_costo = Centro_costo.create(
        nombre=centro_costo_request.nombre,
        descripcion=centro_costo_request.descripcion        
    )
    
    return centro_costo_request

@centro_costo.get('/show/{centro_costo_id}')
async def get_centro_costo(centro_costo_id):
    centro_costo = Centro_costo.select().where(Centro_costo.id == centro_costo_id).first()
    if  centro_costo:
        return Centro_costoResponseModel(id=centro_costo.id,
                                    nombre = centro_costo.nombre,
                                    descripcion = centro_costo.descripcion,
                                )
    else:
        return HTTPException(404, 'Centro de costo no encontrado')
    
@centro_costo.get('/delete/{centro_costo_id}')
async def delete_centro_costo(centro_costo_id):
    centro_costo = Centro_costo.select().where(Centro_costo.id == centro_costo_id).first()
    if  centro_costo:
        centro_costo.delete_instance()
        return {'Centro de costo eliminado'}
    else:
        return HTTPException(404, 'Centro de costo no encontrado')
    
@centro_costo.post('/update/')
async def update_centro_costo(centro_costo_request: Centro_costoUpdateRequestModel):
    centro_costo = Centro_costo.select().where(Centro_costo.id == centro_costo_request.id).first()
    if centro_costo:     
               
        qry=centro_costo.update({Centro_costo.nombre : centro_costo_request.nombre,
                        Centro_costo.descripcion : centro_costo_request.descripcion
                        }).where(Centro_costo.id == centro_costo_request.id)
        qry.execute()
                   
        return {'Centro de costo actualizado'}
    else:
        return HTTPException(404, 'Centro de costo no encontrao')