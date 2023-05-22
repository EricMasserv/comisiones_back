from datetime import date
from pydantic import BaseModel, EmailStr

class VentaUpdateRequestModel(BaseModel):
    id_compania:str
    id_division:str
    id_agente:str
    tipo_asistencia:str
    folio_asistencia:str
    importe_asistencia:str
    empresa_tipo_comision:str
    empresa_comision_importe:str
    division_tipo_comision:str
    division_comision_importe:str
    agente_tipo_comision:str
    agente_comision_importe:str
    metodo:str
    estatus:str
    id:int

class VentaUpdateResponseModel(VentaUpdateRequestModel):
    id:int