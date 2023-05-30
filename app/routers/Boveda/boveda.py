from fastapi import APIRouter
from fastapi import HTTPException
from ...Models.Boveda import Boveda
from ...Schemas.Boveda.BovedaCreateModel import BovedaCreateRequestModel, BovedaResponseModel
from ...Schemas.Boveda.BovedaUpdateModel import BovedaUpdateRequestModel, BovedaUpdateResponseModel
from ...Middlewares.verify_token_route import VerifyTokenRoute

boveda = APIRouter(
    prefix = "/boveda",
    tags = ["Boveda"],
    route_class=VerifyTokenRoute
)

@boveda.post('/create')
async def create_regimenes_fiscales(boveda_request: BovedaCreateRequestModel):
    boveda = Boveda.create(
        nombre=boveda_request.nombre,
        valor=boveda_request.valor,
        descripcion=boveda_request.descripcion        
    )
    
    return boveda_request

@boveda.get('/show/{boveda_id}')
async def get_boveda(boveda_id):
    boveda = Boveda.select().where(Boveda.id == boveda_id).first()
    if  boveda:
        return BovedaResponseModel(id=boveda.id,
                                    nombre = boveda.nombre,
                                    valor = boveda.valor,
                                    descripcion = boveda.descripcion,
                                )
    else:
        return HTTPException(404, 'Boveda no encontrada')

@boveda.get('/show_all')
async def get_boveda_fiscales_all():
    return list(Boveda.select().dicts());
    
@boveda.get('/delete/{boveda_id}')
async def delete_boveda(boveda_id):
    boveda = Boveda.select().where(Boveda.id == boveda_id).first()
    if  boveda:
        boveda.delete_instance()
        return {'Boveda eliminada'}
    else:
        return HTTPException(404, 'Boveda no encontrada')
    
@boveda.post('/update/')
async def update_boveda(boveda_request: BovedaUpdateRequestModel):
    boveda = Boveda.select().where(Boveda.id == boveda_request.id).first()
    if boveda:     
               
        qry=Boveda.update({Boveda.nombre : boveda_request.nombre,
                        Boveda.valor : boveda_request.valor,
                        Boveda.descripcion : boveda_request.descripcion
                        }).where(Boveda.id == boveda_request.id)
        qry.execute()
                   
        return {'Boveda actualizada'}
    else:
        return HTTPException(404, 'Boveda no encontrada')