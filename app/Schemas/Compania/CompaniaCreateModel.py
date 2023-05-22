from datetime import date
from pydantic import BaseModel, EmailStr

class CompanyCreateRequestModel(BaseModel):
    nombre_legal:str
    nombre_compania:str
    regimen_fiscal_id:int
    correo:EmailStr
    contacto_nombre:str
    contacto_correo:EmailStr
    telefono:int
    comision_porcentaje:int
    comision_fija:int
    tipo_pago:int
    dia_maximo_pago_reclamo:int
    dia_pago:int
    fecha_corte:int
    estatus:int
    banco_nombre:str
    banco_numero_cuenta:int
    banco_clabe_bancaria:int
    banco_codigo_swift:int
    banco_codigo_iban:int
    banco_codigo_bic:int
    banco_domicilio:str
    tipo_moneda:int
    contrasena:str
    direccion_legal:str
    direccion_comercial:str

class CompanyResponseModel(CompanyCreateRequestModel):
    id: int