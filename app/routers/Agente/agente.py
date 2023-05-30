from fastapi import APIRouter
from fastapi import HTTPException
from ...Models.Agente import Agente
from ...Models.Usuario import Usuario
from passlib.context import CryptContext
from ...Schemas.Agente.AgenteCreateModel import AgenteCreateRequestModel, AgenteResponseModel
from ...Schemas.Agente.AgenteUpdateModel import AgenteUpdateRequestModel, AgenteUpdateResponseModel
from ...Schemas.Agente.ValidarDocumentos import ValidarDocumentos
from ...Schemas.Agente.AgenteUpdateValidarDocumentos import AgenteUpdateValidarRequestModel
from ...Middlewares.verify_token_route import VerifyTokenRoute
from .Documentos.Guardar_archivos import guardar_archivos
from .Documentos.Validar_ine import validar_ine
from .Documentos.Validar_constancia_fiscal import validar_constancia_fiscal
from .Documentos.Validar_cuenta_bancaria import validar_cuenta_bancaria
from .Documentos.Obtener_datos_constancia_fiscal import obtener_datos_constancia_fiscal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

agente_router = APIRouter(
    prefix = "/agente",
    tags = ["Agente"],
    route_class=VerifyTokenRoute
)

@agente_router.post('/registrar')
async def register_agente(agente_request: AgenteCreateRequestModel):
        usuario = Usuario.create(
            correo=agente_request.correo,
            contrasena=pwd_context.hash(agente_request.contrasena),
            tipo='agente',
            estatus_id= 1        
        )
                
        id_usuario = Usuario.select(Usuario.id).where(Usuario.correo == agente_request.correo).dicts()[0]
    
        agente = Agente.create(
            correo=agente_request.correo,
            contrasena=pwd_context.hash(agente_request.contrasena),
            id_usuario=id_usuario['id'],
        )
        return agente_request
    
@agente_router.post('/validar/documentos')
async def validar_documentos(agente_request: ValidarDocumentos):  
             
    check_ine = True
    bandera_ine = False
    if not await validar_ine(agente_request.ine):
        check_ine = False
        bandera_ine = "El ine ingresado no se puede validar"
        
    check_constancia_fiscal = True
    bandera_constancia_fiscal = False
    if not await validar_constancia_fiscal(agente_request.constancia_fiscal):
        check_constancia_fiscal = False
        bandera_constancia_fiscal = "La constancia fiscal ingresada no se puede validar"
        
    check_cuenta_bancaria = True
    bandera_cuenta_bancaria = False
    if not await validar_cuenta_bancaria(agente_request.cuenta_bancaria):
        check_cuenta_bancaria = False
        bandera_cuenta_bancaria = "La cuenta bancaria ingresada no se puede validar"
                
    if check_ine and check_constancia_fiscal and check_cuenta_bancaria:
        
        ruta_ine = await guardar_archivos(agente_request.ine, "img")
        ruta_constancia_fiscal = await guardar_archivos(agente_request.constancia_fiscal, "pdf")
        ruta_cuenta_bancaria = await guardar_archivos(agente_request.cuenta_bancaria, "img")
        
        datos_pdf = await obtener_datos_constancia_fiscal(agente_request.constancia_fiscal)
                            
        actualizar_usuario = Usuario.update({Usuario.nombre_usuario:f"{datos_pdf['nombres']} {datos_pdf['apellido_pat']} {datos_pdf['apellido_mat']}", Usuario.estatus_id:2}).where(Usuario.id == agente_request.id_usuario)
        actualizar_usuario.execute()
                            
        actualizar_agente = Agente.update({Agente.id_compania:agente_request.id_compania,
                            Agente.id_division:agente_request.id_division,
                            Agente.id_regimen_fiscal:agente_request.id_regimen_fiscal,
                            Agente.nombre_completo:f"{datos_pdf['nombres']} {datos_pdf['apellido_pat']} {datos_pdf['apellido_mat']}",
                            Agente.rfc:datos_pdf['rfc'],
                            Agente.curp:datos_pdf['curp'],
                            Agente.codigo_postal:datos_pdf['codigo_postal'],
                            Agente.calle:datos_pdf['calle'],
                            Agente.no_ext:datos_pdf['no_ext'],
                            Agente.no_int:datos_pdf['no_int'],
                            Agente.colonia:datos_pdf['colonia'],
                            Agente.delegacion_municipio:datos_pdf['delegacion_municipio'],
                            Agente.estado:datos_pdf['estado'],
                            Agente.telefono:agente_request.telefono,
                            Agente.movil:agente_request.movil,
                            Agente.clabe_interbancaria:agente_request.clabe_interbancaria,
                            Agente.id_usuario:agente_request.id_usuario,
                            Agente.ine:ruta_ine,
                            Agente.constancia_fiscal:ruta_constancia_fiscal,
                            Agente.cuenta_bancaria:ruta_cuenta_bancaria
                            }).where(Agente.id_usuario == agente_request.id_usuario)
        actualizar_agente.execute()
        
        return agente_request
            
    else:
        return f"{bandera_ine if bandera_ine else ''}-{bandera_constancia_fiscal if bandera_constancia_fiscal else ''}-{bandera_cuenta_bancaria if bandera_cuenta_bancaria else ''}"

@agente_router.get('/show/{agente_id}')
async def get_agente(agente_id):
    agente = Agente.select().where(Agente.id == agente_id).first()
    if  agente:
        return AgenteResponseModel(id=agente.id,
                                   id_compania=agente.id_compania,
                                   id_division=agente.id_division,
                                   nombre_completo=agente.nombre_completo,
                                   regimen_fiscal_id=agente.regimen_fiscal_id,
                                   rfc=agente.rfc,
                                   correo=agente.correo,
                                   telefono=agente.telefono,
                                   comision_porcentaje=agente.comision_porcentaje,
                                   comision_fija=agente.comision_fija,
                                   tipo_pago=agente.tipo_pago,
                                   dia_maximo_pago_reclamo=agente.dia_maximo_pago_reclamo,
                                   dia_pago=agente.dia_pago,
                                   fecha_corte=agente.fecha_corte,
                                   banco_nombre=agente.banco_nombre,
                                   banco_numero_cuenta=agente.banco_numero_cuenta,
                                   banco_clabe_bancaria=agente.banco_clabe_bancaria,
                                   banco_codigo_swift=agente.banco_codigo_swift,
                                   banco_codigo_iban=agente.banco_codigo_iban,
                                   banco_codigo_bic=agente.banco_codigo_bic,
                                   banco_domicilio=agente.banco_domicilio,
                                   tipo_moneda=agente.tipo_moneda,
                                   contrasena=agente.contrasena,
                                   direccion=agente.direccion,
                                   estatus=agente.estatus
                                 )
    else:
        return HTTPException(404, 'Agente no encontrada')
 
@agente_router.get('/show_all')
async def get_agente_all():
    return list(Agente.select().dicts());
    
@agente_router.get('/delete/{user_id}')
async def delete_agente(user_id):
    agente = Agente.select().where(Agente.id == user_id).first()
    usuario = Usuario.select().where(Usuario.correo == agente.correo).first()
    if  agente:
        agente.delete_instance()
        usuario.delete_instance()
        return {'Agente eliminado'}
    else:
        return HTTPException(404, 'Agente not found')
    
@agente_router.post('/update/')
async def update_agente(agente_request: AgenteUpdateRequestModel):
    agente = Agente.select(Agente.correo).where(Agente.id == agente_request.id).dicts()[0]
    if agente:           
        qry=Agente.update({Agente.id_compania:agente_request.id_compania,
                           Agente.id_division:agente_request.id_division,
                           Agente.nombre_completo:agente_request.nombre_completo,
                           Agente.regimen_fiscal_id:agente_request.regimen_fiscal_id,
                           Agente.rfc:agente_request.rfc,
                           Agente.correo:agente_request.correo,
                           Agente.telefono:agente_request.telefono,
                           Agente.comision_porcentaje:agente_request.comision_porcentaje,
                           Agente.comision_fija:agente_request.comision_fija,
                           Agente.tipo_pago:agente_request.tipo_pago,
                           Agente.dia_maximo_pago_reclamo:agente_request.dia_maximo_pago_reclamo,
                           Agente.dia_pago:agente_request.dia_pago,
                           Agente.fecha_corte:agente_request.fecha_corte,
                           Agente.banco_nombre:agente_request.banco_nombre,
                           Agente.banco_numero_cuenta:agente_request.banco_numero_cuenta,
                           Agente.banco_clabe_bancaria:agente_request.banco_clabe_bancaria,
                           Agente.banco_codigo_swift:agente_request.banco_codigo_swift,
                           Agente.banco_codigo_iban:agente_request.banco_codigo_iban,
                           Agente.banco_codigo_bic:agente_request.banco_codigo_bic,
                           Agente.banco_domicilio:agente_request.banco_domicilio,
                           Agente.tipo_moneda:agente_request.tipo_moneda,
                           Agente.contrasena:pwd_context.hash(agente_request.contrasena),
                           Agente.direccion:agente_request.direccion,
                           Agente.estatus:agente_request.estatus
                             }).where(Agente.id == agente_request.id)
        qry.execute()
        
        qryUser=Usuario.update({Usuario.correo:agente_request.correo,
                                Usuario.contrasena:pwd_context.hash(agente_request.contrasena),
                                Usuario.nombre_usuario:agente_request.nombre_completo,
                             }).where(Usuario.correo == agente['correo'])
        qryUser.execute()
                   
        return {'Agente actualizado'}
    else:
        return HTTPException(404, 'Agente no encontrado')