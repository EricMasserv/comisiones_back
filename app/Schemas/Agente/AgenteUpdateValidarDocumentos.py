from datetime import date
from pydantic import BaseModel, EmailStr

class AgenteUpdateValidarRequestModel(BaseModel):
    id_compania:int
    id_division:int
    id_regimen_fiscal:int
    telefono:str
    movil:str
    banclabe_interbancariaco_nombre:str
    id:int

class AgenteValidarUpdateResponseModel(AgenteUpdateValidarRequestModel):
    id:int