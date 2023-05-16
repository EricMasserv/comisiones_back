from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Compañia import Company
from ..Schemas.CompanyCreateModel import CompanyCreateRequestModel, CompanyResponseModel
from ..Schemas.CompanyUpdateModel import CompanyUpdateRequestModel, CompanyUpdateResponseModel

company_router = APIRouter(
    prefix = "/company",
    tags = ["Company"]
)

@company_router.post('/create')
async def create_company(company_request: CompanyCreateRequestModel):
    company = Company.create(
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
        contraseña=company_request.contraseña,
        direccion_legal=company_request.direccion_legal,
        direccion_comercial=company_request.direccion_comercial,
    )
    return company_request

@company_router.get('/show/{company_id}')
async def get_company(company_id):
    company = Company.select().where(Company.id == company_id).first()
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
                                    contraseña=company.contraseña,
                                    direccion_legal=company.direccion_legal,
                                    direccion_comercial=company.direccion_comercial,
                                 )
    else:
        return HTTPException(404, 'Compañia no encontrada')
    
@company_router.get('/delete/{division_id}')
async def delete_company(division_id):
    company = Company.select().where(Company.id == division_id).first()
    if  company:
        company.delete_instance()
        return {'Compañia eliminada'}
    else:
        return HTTPException(404, 'User not found')
    
@company_router.post('/update/')
async def update_company(company_request: CompanyUpdateRequestModel):
    company = Company.select().where(Company.id == company_request.id).first()
    if company:
        qry=Company.update({Company.nombre_legal:company_request.nombre_legal,
                           Company.nombre_compania:company_request.nombre_compania,
                           Company.regimen_fiscal_id:company_request.regimen_fiscal_id,
                           Company.correo:company_request.correo,
                           Company.contacto_nombre:company_request.contacto_nombre,
                           Company.contacto_correo:company_request.contacto_correo,
                           Company.telefono:company_request.telefono,
                           Company.comision_porcentaje:company_request.comision_porcentaje,
                           Company.comision_fija:company_request.comision_fija,
                           Company.tipo_pago:company_request.tipo_pago,
                           Company.dia_maximo_pago_reclamo:company_request.dia_maximo_pago_reclamo,
                           Company.dia_pago:company_request.dia_pago,
                           Company.fecha_corte:company_request.fecha_corte,
                           Company.estatus:company_request.estatus,
                           Company.banco_nombre:company_request.banco_nombre,
                           Company.banco_numero_cuenta:company_request.banco_numero_cuenta,
                           Company.banco_clabe_bancaria:company_request.banco_clabe_bancaria,
                           Company.banco_codigo_swift:company_request.banco_codigo_swift,
                           Company.banco_codigo_iban:company_request.banco_codigo_iban,
                           Company.banco_codigo_bic:company_request.banco_codigo_bic,
                           Company.banco_domicilio:company_request.banco_domicilio,
                           Company.tipo_moneda:company_request.tipo_moneda,
                           Company.contraseña:company_request.contraseña,
                           Company.direccion_legal:company_request.direccion_legal,
                           Company.direccion_comercial:company_request.direccion_comercial,
                             }).where(Company.id == company_request.id)
        qry.execute()
        
        return {'Compañia actualizada'}
    else:
        return HTTPException(404, 'Compañia no encontrada')