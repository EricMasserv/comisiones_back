from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Company import Company
from ..Schemas.CompanyCreateModel import CompanyCreateRequestModel, CompanyResponseModel
from ..Schemas.CompanyUpdateModel import CompanyUpdateRequestModel, CompanyUpdateResponseModel

company_router = APIRouter(
    prefix = "/company",
    tags = ["Company"]
)

@company_router.post('/create')
async def create_company(company_request: CompanyCreateRequestModel):
    company = Company.create(
        user_id=company_request.user_id,
        legal_name=company_request.legal_name,
        company_name=company_request.company_name,
        tax_regime_id=company_request.tax_regime_id,
        email=company_request.email,
        contact_name=company_request.contact_name,
        contact_email=company_request.contact_email,
        phone=company_request.phone,
        comision_percentage=company_request.comision_percentage,
        comision_fixed=company_request.comision_fixed,
        payment_type=company_request.payment_type,
        claim_payment_max_days=company_request.claim_payment_max_days,
        pay_day=company_request.pay_day,
        cutoff_date=company_request.cutoff_date,
        is_active=company_request.is_active,
        bank_name=company_request.bank_name,
        bank_account_number=company_request.bank_account_number,
        bank_account_clabe=company_request.bank_account_clabe,
        bank_swift=company_request.bank_swift,
        bank_iban=company_request.bank_iban,
        bank_bic=company_request.bank_bic,
        bank_address=company_request.bank_address,
        currency_type=company_request.currency_type,
        password=company_request.password,
        legal_address=company_request.legal_address,
        comercial_address=company_request.comercial_address,
    )
    return company_request

@company_router.get('/show/{company_id}')
async def get_company(company_id):
    company = Company.select().where(Company.id == company_id).first()
    if  company:
        return CompanyResponseModel(id=company.id,
                                    user_id=company.user_id,
                                    legal_name=company.legal_name,
                                    company_name=company.company_name,
                                    tax_regime_id=company.tax_regime_id,
                                    email=company.email,
                                    contact_name=company.contact_name,
                                    contact_email=company.contact_email,
                                    phone=company.phone,
                                    comision_percentage=company.comision_percentage,
                                    comision_fixed=company.comision_fixed,
                                    payment_type=company.payment_type,
                                    claim_payment_max_days=company.claim_payment_max_days,
                                    pay_day=company.pay_day,
                                    cutoff_date=company.cutoff_date,
                                    is_active=company.is_active,
                                    bank_name=company.bank_name,
                                    bank_account_number=company.bank_account_number,
                                    bank_account_clabe=company.bank_account_clabe,
                                    bank_swift=company.bank_swift,
                                    bank_iban=company.bank_iban,
                                    bank_bic=company.bank_bic,
                                    bank_address=company.bank_address,
                                    currency_type=company.currency_type,
                                    password=company.password,
                                    legal_address=company.legal_address,
                                    comercial_address=company.comercial_address,
                                 )
    else:
        return HTTPException(404, 'Compañia no encontrada')
    
@company_router.delete('/delete/{user_id}')
async def delete_company(user_id):
    company = Company.select().where(Company.id == user_id).first()
    if  company:
        company.delete_instance()
        return {'Compañia eliminada'}
    else:
        return HTTPException(404, 'User not found')
    
@company_router.post('/update/')
async def update_company(company_request: CompanyUpdateRequestModel):
    company = Company.select().where(Company.id == company_request.id).first()
    if company:
        company.user_id=company_request.user_id,
        company.legal_name=company_request.legal_name,
        company.company_name=company_request.company_name,
        company.tax_regime_id=company_request.tax_regime_id,
        company.email=company_request.email,
        company.contact_name=company_request.contact_name,
        company.contact_email=company_request.contact_email,
        company.phone=company_request.phone,
        company.comision_percentage=company_request.comision_percentage,
        company.comision_fixed=company_request.comision_fixed,
        company.payment_type=company_request.payment_type,
        company.claim_payment_max_days=company_request.claim_payment_max_days,
        company.pay_day=company_request.pay_day,
        company.cutoff_date=company_request.cutoff_date,
        company.is_active=company_request.is_active,
        company.bank_name=company_request.bank_name,
        company.bank_account_number=company_request.bank_account_number,
        company.bank_account_clabe=company_request.bank_account_clabe,
        company.bank_swift=company_request.bank_swift,
        company.bank_iban=company_request.bank_iban,
        company.bank_bic=company_request.bank_bic,
        company.bank_address=company_request.bank_address,
        company.currency_type=company_request.currency_type,
        company.password=company_request.password,
        company.legal_address=company_request.legal_address,
        company.comercial_address=company_request.comercial_address,
        company.save()
        return {'Compañia actualizada'}
    else:
        return HTTPException(404, 'Compañia no encontrada')