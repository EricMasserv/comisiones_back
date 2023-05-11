from ..Database.database import database 
from peewee import *
from datetime import datetime

class Company(Model):
    user_id = BigIntegerField(null=True)
    """ adn = CharField(max_length=255,null=True) """
    legal_name = CharField(max_length=255,null=True)
    company_name = CharField(max_length=255,null=True)
    tax_regime_id = BigIntegerField(null=True)
    """ tax_id = CharField(max_length=255,null=True) """
    email = CharField(max_length=255,null=True)
    contact_name = CharField(max_length=255,null=True)
    contact_email = CharField(max_length=255,null=True)
    phone = CharField(max_length=255,null=True)
    comision_percentage = CharField(max_length=255,null=True)
    comision_fixed = DoubleField(null=True)
    payment_type = CharField(max_length=255,null=True)
    claim_payment_max_days = CharField(max_length=255,null=True)
    pay_day = BigIntegerField(null=True)
    cutoff_date = CharField(max_length=255,null=True)
    is_active = BooleanField(null=False)
    bank_name = CharField(max_length=255,null=True)
    bank_account_number = CharField(max_length=255,null=True)
    bank_account_clabe = CharField(max_length=255,null=True)
    bank_swift = CharField(max_length=255,null=True)
    bank_iban = CharField(max_length=255,null=True)
    bank_bic = CharField(max_length=255,null=True)
    bank_address = CharField(max_length=255,null=True)
    currency_type = CharField(max_length=255,null=True)
    password = CharField(max_length=255,null=True)
    legal_address = CharField(max_length=255,null=True)
    comercial_address = CharField(max_length=255,null=True)
    remember_token = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()

    def __str__(self):
        return self.company_name
    
    class Meta:
        database = database
        table_name = 'companies'

