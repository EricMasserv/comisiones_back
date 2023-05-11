from datetime import date
from pydantic import BaseModel, EmailStr

class CompanyCreateRequestModel(BaseModel):
    user_id:int
    legal_name:str
    company_name:str
    tax_regime_id:int
    email:EmailStr
    contact_name:str
    contact_email:EmailStr
    phone:int
    comision_percentage:int
    comision_fixed:int
    payment_type:int
    claim_payment_max_days:int
    pay_day:int
    cutoff_date:int
    is_active:int
    bank_name:str
    bank_account_number:int
    bank_account_clabe:int
    bank_swift:int
    bank_iban:int
    bank_bic:int
    bank_address:str
    currency_type:int
    password:str
    legal_address:str
    comercial_address:str

class CompanyResponseModel(CompanyCreateRequestModel):
    id: int