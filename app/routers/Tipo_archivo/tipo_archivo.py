from fastapi import APIRouter
from fastapi import HTTPException
from ...Models.Tipo_archivo import Tipo_archivo
from ...Schemas.Tipo_archivo.Tipo_archivoCreateModel import TipoArchivoCreateRequestModel, TipoArchivoResponseModel
from ...Schemas.Tipo_archivo.Tipo_archivoUpdateModel import TipoArchivoUpdateRequestModel, TipoArchivoUpdateResponseModel
from ...Middlewares.verify_token_route import VerifyTokenRoute

tipo_archivo_router = APIRouter(
    prefix = "/tipo_archivo",
    tags = ["Tipo_archivo"],
    route_class=VerifyTokenRoute
)

@tipo_archivo_router.post('/create')
async def create_tipo_archivo(tipo_archivo_request: TipoArchivoCreateRequestModel):
    tipo_archivo = Tipo_archivo.create(
        nombre=tipo_archivo_request.nombre,
        descripcion=tipo_archivo_request.descripcion
    )
    
    return tipo_archivo_request

@tipo_archivo_router.get('/show/{tipo_archivo_id}')
async def get_tipo_archivo(tipo_archivo_id):
    tipo_archivo = Tipo_archivo.select().where(Tipo_archivo.id == tipo_archivo_id).first()
    if  tipo_archivo:
        return TipoArchivoResponseModel(id=tipo_archivo.id,
                                        nombre=tipo_archivo.nombre,
                                        descripcion=tipo_archivo.descripcion
                                 )
    else:
        return HTTPException(404, 'Tipo de archivo no encontrado')

@tipo_archivo_router.get('/show_all')
async def get_tipo_archivo_all():
    return list(Tipo_archivo.select().dicts());
    
@tipo_archivo_router.get('/delete/{tipo_archivo_id}')
async def delete_tipo_archivo(tipo_archivo_id):
    tipo_archivo = Tipo_archivo.select().where(Tipo_archivo.id == tipo_archivo_id).first()
    if  tipo_archivo:
        tipo_archivo.delete_instance()
        return {'Tipo de archivo eliminado'}
    else:
        return HTTPException(404, 'Tipo de archivo no encontrado')
    
@tipo_archivo_router.post('/update/')
async def update_tipo_archivo(tipo_archivo_request: TipoArchivoUpdateRequestModel):
    producto = Tipo_archivo.select().where(Tipo_archivo.id == tipo_archivo_request.id).first()
    if producto:     
               
        qry=Tipo_archivo.update({Tipo_archivo.nombre:tipo_archivo_request.nombre,
                                 Tipo_archivo.descripcion:tipo_archivo_request.descripcion
                             }).where(Tipo_archivo.id == tipo_archivo_request.id)
        qry.execute()
                   
        return {'Tipo de archivo actualizado'}
    else:
        return HTTPException(404, 'Tipo de archivo no encontrado')