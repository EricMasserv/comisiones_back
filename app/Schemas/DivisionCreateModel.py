from datetime import date
from pydantic import BaseModel, EmailStr

class DivisionCreateRequestModel(BaseModel):
    id_compania:int
    nombre_division:str
    regimen_fiscal_id:int
    rfc:str
    correo:str
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
    contraseña:str
    direccion:str
    estatus:int
    
class DivisionResponseModel(DivisionCreateRequestModel):
    id:int

    
    