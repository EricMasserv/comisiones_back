from datetime import date
from pydantic import BaseModel, EmailStr

class DivisionUpdateRequestModel(BaseModel):
    id_compania:int
    nombre_division:str
    regimen_fiscal_id:int
    rfc:str
    correo:EmailStr
    telefono:str
    comision_porcentaje:int
    comision_fija:int
    tipo_pago:int
    dia_maximo_pago_reclamo:int
    dia_pago:date
    fecha_corte:date
    banco_nombre:str
    banco_numero_cuenta:int
    banco_clabe_bancaria:int
    banco_codigo_swift:int
    banco_codigo_iban:int
    banco_codigo_bic:int
    banco_domicilio:str
    tipo_moneda:str
    contrasena:str
    direccion:str
    estatus:int
    id:int

class DivisionUpdateResponseModel(DivisionUpdateRequestModel):
    id:int