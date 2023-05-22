from datetime import date
from pydantic import BaseModel, EmailStr

class ProductoUpdateRequestModel(BaseModel):
    id_compania:int
    id_compania_mass:int
    id_plan_mass:int
    nombre:str
    precio:int
    comision_porcentaje:int
    comision_fija:int
    limite_superior:int
    limite_inferior:int
    estatus:int
    id:int

class ProductoUpdateResponseModel(ProductoUpdateRequestModel):
    id:int