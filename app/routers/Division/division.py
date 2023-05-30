from fastapi import APIRouter
from fastapi import HTTPException
from ...Models.Division import Division
from ...Models.Usuario import Usuario
from passlib.context import CryptContext
from ...Schemas.Division.DivisionCreateModel import DivisionCreateRequestModel, DivisionResponseModel
from ...Schemas.Division.DivisionUpdateModel import DivisionUpdateRequestModel, DivisionUpdateResponseModel
from ...Middlewares.verify_token_route import VerifyTokenRoute

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

division_router = APIRouter(
    prefix = "/division",
    tags = ["Division"],
    route_class=VerifyTokenRoute
)

@division_router.post('/create')
async def create_division(division_request: DivisionCreateRequestModel):
    usuario = Usuario.create(
        correo=division_request.correo,
        nombre_usuario='Division',
        contrasena=pwd_context.hash(division_request.contrasena),
        tipo='division'        
    )
    
    id_usuario = Usuario.select(Usuario.id).where(Usuario.correo == division_request.correo).dicts()[0]
    
    division = Division.create(
        id_compania=division_request.id_compania,
        nombre_division=division_request.nombre_division,
        regimen_fiscal_id=division_request.regimen_fiscal_id,
        rfc=division_request.rfc,
        correo=division_request.correo,
        telefono=division_request.telefono,
        comision_porcentaje=division_request.comision_porcentaje,
        comision_fija=division_request.comision_fija,
        tipo_pago=division_request.tipo_pago,
        dia_maximo_pago_reclamo=division_request.dia_maximo_pago_reclamo,
        dia_pago=division_request.dia_pago,
        fecha_corte=division_request.fecha_corte,
        banco_nombre=division_request.banco_nombre,
        banco_numero_cuenta=division_request.banco_numero_cuenta,
        banco_clabe_bancaria=division_request.banco_clabe_bancaria,
        banco_codigo_swift=division_request.banco_codigo_swift,
        banco_codigo_iban=division_request.banco_codigo_iban,
        banco_codigo_bic=division_request.banco_codigo_bic,
        banco_domicilio=division_request.banco_domicilio,
        tipo_moneda=division_request.tipo_moneda,
        contrasena=pwd_context.hash(division_request.contrasena),
        direccion=division_request.direccion,
        estatus=division_request.estatus,
        id_usuario=id_usuario['id']
    )
    
    return division_request

@division_router.get('/show/{division_id}')
async def get_division(division_id):
    division = Division.select().where(Division.id == division_id).first()
    if  division:
        return DivisionResponseModel(id=division.id,
                                    id_compania=division.id_compania,
                                    nombre_division=division.nombre_division,
                                    regimen_fiscal_id=division.regimen_fiscal_id,
                                    rfc=division.rfc,
                                    correo=division.correo,
                                    telefono=division.telefono,
                                    comision_porcentaje=division.comision_porcentaje,
                                    comision_fija=division.comision_fija,
                                    tipo_pago=division.tipo_pago,
                                    dia_maximo_pago_reclamo=division.dia_maximo_pago_reclamo,
                                    dia_pago=division.dia_pago,
                                    fecha_corte=division.fecha_corte,
                                    banco_nombre=division.banco_nombre,
                                    banco_numero_cuenta=division.banco_numero_cuenta,
                                    banco_clabe_bancaria=division.banco_clabe_bancaria,
                                    banco_codigo_swift=division.banco_codigo_swift,
                                    banco_codigo_iban=division.banco_codigo_iban,
                                    banco_codigo_bic=division.banco_codigo_bic,
                                    banco_domicilio=division.banco_domicilio,
                                    tipo_moneda=division.tipo_moneda,
                                    contrasena=division.contrasena,
                                    direccion=division.direccion,
                                    estatus=division.estatus
                                 )
    else:
        return HTTPException(404, 'Division no encontrada')

@division_router.get('/show_all')
async def get_division_all():
    return list(Division.select().dicts());
    
@division_router.get('/delete/{division_id}')
async def delete_division(division_id):
    division = Division.select().where(Division.id == division_id).first()
    usuario = Usuario.select().where(Usuario.correo == division.correo).first()
    if  division:
        division.delete_instance()
        usuario.delete_instance()
        return {'Division eliminada'}
    else:
        return HTTPException(404, 'Division not found')
    
@division_router.post('/update/')
async def update_division(division_request: DivisionUpdateRequestModel):
    division = Division.select(Division.correo).where(Division.id == division_request.id).dicts()[0]
    if division:              
        qry=Division.update({Division.id_compania:division_request.id_compania,
                             Division.nombre_division:division_request.nombre_division,
                             Division.regimen_fiscal_id:division_request.regimen_fiscal_id,
                             Division.rfc:division_request.rfc,
                             Division.correo:division_request.correo,
                             Division.telefono:division_request.telefono,
                             Division.comision_porcentaje:division_request.comision_porcentaje,
                             Division.comision_fija:division_request.comision_fija,
                             Division.tipo_pago:division_request.tipo_pago,
                             Division.dia_maximo_pago_reclamo:division_request.dia_maximo_pago_reclamo,
                             Division.dia_pago:division_request.dia_pago,
                             Division.fecha_corte:division_request.fecha_corte,
                             Division.banco_nombre:division_request.banco_nombre,
                             Division.banco_numero_cuenta:division_request.banco_numero_cuenta,
                             Division.banco_clabe_bancaria:division_request.banco_clabe_bancaria,
                             Division.banco_codigo_swift:division_request.banco_codigo_swift,
                             Division.banco_codigo_iban:division_request.banco_codigo_iban,
                             Division.banco_codigo_bic:division_request.banco_codigo_bic,
                             Division.banco_domicilio:division_request.banco_domicilio,
                             Division.tipo_moneda:division_request.tipo_moneda,
                             Division.contrasena:pwd_context.hash(division_request.contrasena),
                             Division.direccion:division_request.direccion,
                             Division.estatus:division_request.estatus
                             }).where(Division.id == division_request.id)
        qry.execute()
        qryUser=Usuario.update({Usuario.correo:division_request.correo,
                                Usuario.contrasena:pwd_context.hash(division_request.contrasena),
                             }).where(Usuario.correo == division['correo'])
        qryUser.execute()
                   
        return {'Division actualizada'}
    else:
        return HTTPException(404, 'Division no encontrada')