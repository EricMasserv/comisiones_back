from ..Database.database import database 
from peewee import *
from datetime import datetime

class Division(Model):
    id_compania = IntegerField(null=True)
    nombre_division = CharField(max_length=255,null=True)
    regimen_fiscal_id = IntegerField(null=True)
    rfc = CharField(max_length=255,null=True)
    correo = CharField(max_length=255,null=True)
    telefono = CharField(max_length=255,null=True)
    comision_porcentaje = IntegerField(null=True)
    comision_fija = IntegerField(null=True)
    tipo_pago = IntegerField(null=True)
    dia_maximo_pago_reclamo = IntegerField(null=True)
    dia_pago = DateTimeField()
    fecha_corte = DateTimeField()
    banco_nombre = CharField(max_length=255,null=True)
    banco_numero_cuenta = IntegerField(null=True)
    banco_clabe_bancaria = IntegerField(null=True)
    banco_codigo_swift = IntegerField(null=True)
    banco_codigo_iban = IntegerField(null=True)
    banco_codigo_bic = IntegerField(null=True)
    banco_domicilio = CharField(max_length=255,null=True)
    tipo_moneda = CharField(max_length=255,null=True)
    contrasena = CharField(max_length=255,null=True)
    direccion = CharField(max_length=255,null=True)
    estatus = IntegerField(null=True)
    id_usuario = IntegerField(null=True)
    remember_token = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()

    def __str__(self):
        return self.nombre_division
    
    class Meta:
        database = database
        table_name = 'divisions'
