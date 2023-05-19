from ..Database.database import database 
from peewee import *
from datetime import datetime

class Compania(Model):
    nombre_legal = CharField(max_length=255,null=True)
    nombre_compania = CharField(max_length=255,null=True)
    regimen_fiscal_id = BigIntegerField(null=True)
    correo = CharField(max_length=255,null=True)
    contacto_nombre = CharField(max_length=255,null=True)
    contacto_correo = CharField(max_length=255,null=True)
    telefono = CharField(max_length=255,null=True)
    comision_porcentaje = CharField(max_length=255,null=True)
    comision_fija = DoubleField(null=True)
    tipo_pago = CharField(max_length=255,null=True)
    dia_maximo_pago_reclamo = CharField(max_length=255,null=True)
    dia_pago = BigIntegerField(null=True)
    fecha_corte = CharField(max_length=255,null=True)
    estatus = BooleanField(null=False)
    banco_nombre = CharField(max_length=255,null=True)
    banco_numero_cuenta = CharField(max_length=255,null=True)
    banco_clabe_bancaria = CharField(max_length=255,null=True)
    banco_codigo_swift = CharField(max_length=255,null=True)
    banco_codigo_iban = CharField(max_length=255,null=True)
    banco_codigo_bic = CharField(max_length=255,null=True)
    banco_domicilio = CharField(max_length=255,null=True)
    tipo_moneda = CharField(max_length=255,null=True)
    contrasena = CharField(max_length=255,null=True)
    direccion_legal = CharField(max_length=255,null=True)
    direccion_comercial = CharField(max_length=255,null=True)
    id_usuario = IntegerField(null=True)
    remember_token = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()

    def __str__(self):
        return self.nombre_compania
    
    class Meta:
        database = database
        table_name = 'companias'

