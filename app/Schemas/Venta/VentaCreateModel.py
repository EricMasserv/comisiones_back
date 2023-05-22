from datetime import date
from pydantic import BaseModel, EmailStr

class VentaCreateRequestModel(BaseModel):
    id_compania:int
    id_division:int
    id_agente:int
    tipo_asistencia:str
    folio_asistencia:str
    importe_asistencia:int
    empresa_tipo_comision:str
    empresa_comision_importe:int
    division_tipo_comision:str
    division_comision_importe:int
    agente_tipo_comision:str
    agente_comision_importe:int
    metodo:str
    estatus:int
    
class VentaResponseModel(VentaCreateRequestModel):
    id:int

    
    