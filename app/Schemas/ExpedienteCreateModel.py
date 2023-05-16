from datetime import date
from pydantic import BaseModel, EmailStr

class ExpedienteCreateRequestModel(BaseModel):
    id_compania:int
    id_division:int
    id_agente:int
    id_tipo_archivo:str
    ruta:str
    estatus:int
    
class ExpedienteResponseModel(ExpedienteCreateRequestModel):
    id:int

    
    