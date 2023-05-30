from fastapi import APIRouter
from fastapi import HTTPException
from ...Models.Regimenes_fiscales import Regimenes_fiscales
from ...Schemas.Regimen_fiscal.Regimenes_fiscalesCreateModel import Regimenes_fiscalesCreateRequestModel, Regimenes_fiscalesResponseModel
from ...Schemas.Regimen_fiscal.Regimenes_fiscalesUpdateModel import Regimenes_fiscalesUpdateRequestModel, Regimenes_fiscalesUpdateResponseModel
from ...Middlewares.verify_token_route import VerifyTokenRoute

regimenes_fiscales = APIRouter(
    prefix = "/regimenes_fiscales",
    tags = ["Regimenes_fiscales"],
    route_class=VerifyTokenRoute
)

@regimenes_fiscales.post('/create')
async def create_regimenes_fiscales(regimenes_fiscales_request: Regimenes_fiscalesCreateRequestModel):
    regimenes_fiscales = Regimenes_fiscales.create(
        codigo=regimenes_fiscales_request.codigo,
        nombre=regimenes_fiscales_request.nombre,
        descripcion=regimenes_fiscales_request.descripcion        
    )
    
    return regimenes_fiscales_request

@regimenes_fiscales.get('/show/{venta_id}')
async def get_regimenes_fiscales(venta_id):
    regimenes_fiscales = Regimenes_fiscales.select().where(Regimenes_fiscales.id == venta_id).first()
    if  regimenes_fiscales:
        return Regimenes_fiscalesResponseModel(id=regimenes_fiscales.id,
                                codigo = regimenes_fiscales.codigo,
                                nombre = regimenes_fiscales.nombre,
                                descripcion = regimenes_fiscales.descripcion,
                                )
    else:
        return HTTPException(404, 'El regimen fiscal no se encontra')

@regimenes_fiscales.get('/show_all')
async def get_regimenes_fiscales_all():
    return list(Regimenes_fiscales.select().dicts());
    
@regimenes_fiscales.get('/delete/{regimenes_fiscales_id}')
async def delete_regimenes_fiscales(regimenes_fiscales_id):
    regimenes_fiscales = Regimenes_fiscales.select().where(Regimenes_fiscales.id == regimenes_fiscales_id).first()
    if  regimenes_fiscales:
        regimenes_fiscales.delete_instance()
        return {'Regimen fiscal eliminado'}
    else:
        return HTTPException(404, 'Regimen fiscal no encontrado')
    
@regimenes_fiscales.post('/update/')
async def update_regimenes_fiscales(regimenes_fiscales_request: Regimenes_fiscalesUpdateRequestModel):
    regimenes_fiscales = Regimenes_fiscales.select().where(regimenes_fiscales_request.id == regimenes_fiscales_request.id).first()
    if regimenes_fiscales:     
               
        qry=Regimenes_fiscales.update({Regimenes_fiscales.codigo : regimenes_fiscales_request.codigo,
                        Regimenes_fiscales.nombre : regimenes_fiscales_request.nombre,
                        Regimenes_fiscales.descripcion : regimenes_fiscales_request.descripcion
                        }).where(Regimenes_fiscales.id == regimenes_fiscales_request.id)
        qry.execute()
                   
        return {'El regimen fiscal ha sido actualizado'}
    else:
        return HTTPException(404, 'Regimen fiscal no encontrada')