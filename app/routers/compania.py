from fastapi import APIRouter, HTTPException, Depends
from ..Models.Compania import Compania
from ..Models.Usuario import Usuario
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..Schemas.CompaniaCreateModel import CompanyCreateRequestModel, CompanyResponseModel
from ..Schemas.CompaniaUpdateModel import CompanyUpdateRequestModel, CompanyUpdateResponseModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

compania_router = APIRouter(
    prefix = "/compania",
    tags = ["Company"]
)

oauth2_scheme = OAuth2PasswordBearer("/token")

@compania_router.get('/prueba')
async def prueba(token:str = Depends(oauth2_scheme)):
    return 'holi'

@compania_router.post('/create')
async def create_company(company_request: CompanyCreateRequestModel):
    usuario = Usuario.create(
        correo=company_request.correo,
        contrasena=pwd_context.hash(company_request.contrasena),
        tipo='compania'        
    )
    
    id_usuario = Usuario.select(Usuario.id).where(Usuario.correo == company_request.correo).dicts()[0]

    company = Compania.create(
        nombre_legal=company_request.nombre_legal,
        nombre_compania=company_request.nombre_compania,
        regimen_fiscal_id=company_request.regimen_fiscal_id,
        correo=company_request.correo,
        contacto_nombre=company_request.contacto_nombre,
        contacto_correo=company_request.contacto_correo,
        telefono=company_request.telefono,
        comision_porcentaje=company_request.comision_porcentaje,
        comision_fija=company_request.comision_fija,
        tipo_pago=company_request.tipo_pago,
        dia_maximo_pago_reclamo=company_request.dia_maximo_pago_reclamo,
        dia_pago=company_request.dia_pago,
        fecha_corte=company_request.fecha_corte,
        estatus=company_request.estatus,
        banco_nombre=company_request.banco_nombre,
        banco_numero_cuenta=company_request.banco_numero_cuenta,
        banco_clabe_bancaria=company_request.banco_clabe_bancaria,
        banco_codigo_swift=company_request.banco_codigo_swift,
        banco_codigo_iban=company_request.banco_codigo_iban,
        banco_codigo_bic=company_request.banco_codigo_bic,
        banco_domicilio=company_request.banco_domicilio,
        tipo_moneda=company_request.tipo_moneda,
        contrasena=pwd_context.hash(company_request.contrasena),
        direccion_legal=company_request.direccion_legal,
        direccion_comercial=company_request.direccion_comercial,
        id_usuario=id_usuario['id']
    )
    return company_request

@compania_router.get('/show/{company_id}')
async def get_company(company_id):
    company = Compania.select().where(Compania.id == company_id).first()
    if  company:
        return CompanyResponseModel(id=company.id,
                                    nombre_legal=company.nombre_legal,
                                    nombre_compania=company.nombre_compania,
                                    regimen_fiscal_id=company.regimen_fiscal_id,
                                    correo=company.correo,
                                    contacto_nombre=company.contacto_nombre,
                                    contacto_correo=company.contacto_correo,
                                    telefono=company.telefono,
                                    comision_porcentaje=company.comision_porcentaje,
                                    comision_fija=company.comision_fija,
                                    tipo_pago=company.tipo_pago,
                                    dia_maximo_pago_reclamo=company.dia_maximo_pago_reclamo,
                                    dia_pago=company.dia_pago,
                                    fecha_corte=company.fecha_corte,
                                    estatus=company.estatus,
                                    banco_nombre=company.banco_nombre,
                                    banco_numero_cuenta=company.banco_numero_cuenta,
                                    banco_clabe_bancaria=company.banco_clabe_bancaria,
                                    banco_codigo_swift=company.banco_codigo_swift,
                                    banco_codigo_iban=company.banco_codigo_iban,
                                    banco_codigo_bic=company.banco_codigo_bic,
                                    banco_domicilio=company.banco_domicilio,
                                    tipo_moneda=company.tipo_moneda,
                                    contrasena=company.contrasena,
                                    direccion_legal=company.direccion_legal,
                                    direccion_comercial=company.direccion_comercial,
                                 )
    else:
        return HTTPException(404, 'Compañia no encontrada')
    
@compania_router.get('/delete/{division_id}')
async def delete_company(division_id):
    company = Compania.select().where(Compania.id == division_id).first()
    usuario = Usuario.select().where(Usuario.correo == company.correo).first()
    if  company:
        company.delete_instance()
        usuario.delete_instance()
        return {'Compañia eliminada'}
    else:
        return HTTPException(404, 'User not found')
    
@compania_router.post('/update/')
async def update_company(company_request: CompanyUpdateRequestModel):
    compania = Compania.select(Compania.correo).where(Compania.id == company_request.id).dicts()[0]
    if compania:
        qry=Compania.update({Compania.nombre_legal:company_request.nombre_legal,
                           Compania.nombre_compania:company_request.nombre_compania,
                           Compania.regimen_fiscal_id:company_request.regimen_fiscal_id,
                           Compania.correo:company_request.correo,
                           Compania.contacto_nombre:company_request.contacto_nombre,
                           Compania.contacto_correo:company_request.contacto_correo,
                           Compania.telefono:company_request.telefono,
                           Compania.comision_porcentaje:company_request.comision_porcentaje,
                           Compania.comision_fija:company_request.comision_fija,
                           Compania.tipo_pago:company_request.tipo_pago,
                           Compania.dia_maximo_pago_reclamo:company_request.dia_maximo_pago_reclamo,
                           Compania.dia_pago:company_request.dia_pago,
                           Compania.fecha_corte:company_request.fecha_corte,
                           Compania.estatus:company_request.estatus,
                           Compania.banco_nombre:company_request.banco_nombre,
                           Compania.banco_numero_cuenta:company_request.banco_numero_cuenta,
                           Compania.banco_clabe_bancaria:company_request.banco_clabe_bancaria,
                           Compania.banco_codigo_swift:company_request.banco_codigo_swift,
                           Compania.banco_codigo_iban:company_request.banco_codigo_iban,
                           Compania.banco_codigo_bic:company_request.banco_codigo_bic,
                           Compania.banco_domicilio:company_request.banco_domicilio,
                           Compania.tipo_moneda:company_request.tipo_moneda,
                           Compania.contrasena:pwd_context.hash(company_request.contrasena),
                           Compania.direccion_legal:company_request.direccion_legal,
                           Compania.direccion_comercial:company_request.direccion_comercial,
                             }).where(Compania.id == company_request.id)
        qry.execute()
        
        qryUser=Usuario.update({Usuario.correo:company_request.correo,
                                Usuario.contrasena:pwd_context.hash(company_request.contrasena),
                             }).where(Usuario.correo == compania['correo'])
        qryUser.execute()
                
        return {'Compañia actualizada'}
    else:
        return HTTPException(404, 'Compañia no encontrada')