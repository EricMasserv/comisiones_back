from datetime import date
from pydantic import BaseModel, EmailStr

class ExpedienteUpdateRequestModel(BaseModel):
    id_compania:int
    id_division:int
    id_agente:int
    id_tipo_archivo:str
    ruta:str
    estatus:int
    id:int

class ExpedienteUpdateResponseModel(ExpedienteUpdateRequestModel):
    id:int