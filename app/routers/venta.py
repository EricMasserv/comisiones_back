from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Venta import Venta
from ..Schemas.Venta.VentaCreateModel import VentaCreateRequestModel, VentaResponseModel
from ..Schemas.Venta.VentaUpdateModel import VentaUpdateRequestModel, VentaUpdateResponseModel
from ..Middlewares.verify_token_route import VerifyTokenRoute

venta_router = APIRouter(
    prefix = "/venta",
    tags = ["Venta"],
    route_class=VerifyTokenRoute
)

@venta_router.post('/create')
async def create_tipo_archivo(venta_request: VentaCreateRequestModel):
    venta = Venta.create(
        id_compania=venta_request.id_compania,
        id_division=venta_request.id_division,
        id_agente=venta_request.id_agente,
        tipo_asistencia=venta_request.tipo_asistencia,
        folio_asistencia=venta_request.folio_asistencia,
        importe_asistencia=venta_request.importe_asistencia,
        empresa_tipo_comision=venta_request.empresa_tipo_comision,
        empresa_comision_importe=venta_request.empresa_comision_importe,
        division_tipo_comision=venta_request.division_tipo_comision,
        division_comision_importe=venta_request.division_comision_importe,
        agente_tipo_comision=venta_request.agente_tipo_comision,
        agente_comision_importe=venta_request.agente_comision_importe,
        metodo=venta_request.metodo,
        estatus=venta_request.estatus
        
    )
    
    return venta_request

@venta_router.get('/show/{venta_id}')
async def get_venta(venta_id):
    venta = Venta.select().where(Venta.id == venta_id).first()
    if  venta:
        return VentaResponseModel(id=venta.id,
                                id_compania = venta.id_compania,
                                id_division = venta.id_division,
                                id_agente = venta.id_agente,
                                tipo_asistencia = venta.tipo_asistencia,
                                folio_asistencia = venta.folio_asistencia,
                                importe_asistencia = venta.importe_asistencia,
                                empresa_tipo_comision = venta.empresa_tipo_comision,
                                empresa_comision_importe = venta.empresa_comision_importe,
                                division_tipo_comision = venta.division_tipo_comision,
                                division_comision_importe = venta.division_comision_importe,
                                agente_tipo_comision = venta.agente_tipo_comision,
                                agente_comision_importe = venta.agente_comision_importe,
                                metodo = venta.metodo,
                                estatus = venta.estatus,
                                )
    else:
        return HTTPException(404, 'Venta no encontrada')
    
@venta_router.get('/delete/{venta_id}')
async def delete_venta(venta_id):
    venta = Venta.select().where(Venta.id == venta_id).first()
    if  venta:
        venta.delete_instance()
        return {'Venta de archivo eliminado'}
    else:
        return HTTPException(404, 'TVenta no encontrada')
    
@venta_router.post('/update/')
async def update_venta(venta_request: VentaUpdateRequestModel):
    venta = Venta.select().where(Venta.id == venta_request.id).first()
    if venta:     
               
        qry=Venta.update({Venta.id_compania : venta_request.id_compania,
                        Venta.id_division : venta_request.id_division,
                        Venta.id_agente : venta_request.id_agente,
                        Venta.tipo_asistencia : venta_request.tipo_asistencia,
                        Venta.folio_asistencia : venta_request.folio_asistencia,
                        Venta.importe_asistencia : venta_request.importe_asistencia,
                        Venta.empresa_tipo_comision : venta_request.empresa_tipo_comision,
                        Venta.empresa_comision_importe : venta_request.empresa_comision_importe,
                        Venta.division_tipo_comision : venta_request.division_tipo_comision,
                        Venta.division_comision_importe : venta_request.division_comision_importe,
                        Venta.agente_tipo_comision : venta_request.agente_tipo_comision,
                        Venta.agente_comision_importe : venta_request.agente_comision_importe,
                        Venta.metodo : venta_request.metodo,
                        Venta.estatus : venta_request.estatus,
                          
                          
                          
                        }).where(Venta.id == venta_request.id)
        qry.execute()
                   
        return {'Tipo de archivo actualizado'}
    else:
        return HTTPException(404, 'Venta no encontrada')