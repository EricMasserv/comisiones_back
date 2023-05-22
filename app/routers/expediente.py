from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Expediente import Expediente
from ..Schemas.Expediente.ExpedienteCreateModel import ExpedienteCreateRequestModel, ExpedienteResponseModel
from ..Schemas.Expediente.ExpedienteUpdateModel import ExpedienteUpdateRequestModel, ExpedienteUpdateResponseModel
from ..Middlewares.verify_token_route import VerifyTokenRoute

expediente_router = APIRouter(
    prefix = "/expediente",
    tags = ["Expediente"],
    route_class=VerifyTokenRoute
)

@expediente_router.post('/create')
async def create_expediente(expediente_request: ExpedienteCreateRequestModel):
    expediente = Expediente.create(
        id_compania=expediente_request.id_compania,
        id_division=expediente_request.id_division,
        id_agente=expediente_request.id_agente,
        id_tipo_archivo=expediente_request.id_tipo_archivo,
        ruta=expediente_request.ruta,
        estatus=expediente_request.estatus
    )
    
    return expediente_request

@expediente_router.get('/show/{expediente_id}')
async def get_expediente(expediente_id):
    expediente = Expediente.select().where(Expediente.id == expediente_id).first()
    if  expediente:
        return ExpedienteResponseModel(id=expediente.id,
                                    id_compania=expediente.id_compania,
                                    id_division=expediente.id_division,
                                    id_agente=expediente.id_agente,
                                    id_tipo_archivo=expediente.id_tipo_archivo,
                                    ruta=expediente.ruta,
                                    estatus=expediente.estatus
                                 )
    else:
        return HTTPException(404, 'Expediente no encontrado')
    
@expediente_router.get('/delete/{expediente_id}')
async def delete_expediente(expediente_id):
    expediente = Expediente.select().where(Expediente.id == expediente_id).first()
    if  expediente:
        expediente.delete_instance()
        return {'Expediente eliminada'}
    else:
        return HTTPException(404, 'Expediente not found')
    
@expediente_router.post('/update/')
async def update_expediente(expediente_request: ExpedienteUpdateRequestModel):
    expediente = Expediente.select().where(Expediente.id == expediente_request.id).first()
    if expediente:     
               
        qry=Expediente.update({Expediente.id_compania:expediente_request.id_compania,
                             Expediente.id_division:expediente_request.id_division,
                             Expediente.id_agente:expediente_request.id_agente,
                             Expediente.id_tipo_archivo:expediente_request.id_tipo_archivo,
                             Expediente.ruta:expediente_request.ruta,
                             Expediente.estatus:expediente_request.estatus
                             }).where(Expediente.id == expediente_request.id)
        qry.execute()
                   
        return {'Expediente actualizada'}
    else:
        return HTTPException(404, 'Expediente no encontrada')