from datetime import date
from pydantic import BaseModel, EmailStr

class ValidarDocumentos(BaseModel):
    id_compania:int
    id_division:int
    id_regimen_fiscal:int
    telefono:str
    movil:str
    clabe_interbancaria:str
    id_usuario:int
    ine:str
    constancia_fiscal:str
    cuenta_bancaria:str
    
class AgenteCreateValidarResponseModel(ValidarDocumentos):
    id:int

    
    