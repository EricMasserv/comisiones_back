from ..Database.database import database 
from peewee import *
from datetime import datetime

class Agente(Model):
    id_compania = IntegerField(null=True)
    id_division = IntegerField(null=True)
    id_regimen_fiscal = IntegerField(null=True)
    nombre_completo = CharField(max_length=255,null=True)
    rfc = CharField(max_length=255,null=True)
    curp = CharField(max_length=255,null=True)
    codigo_postal = CharField(max_length=255,null=True)
    calle = CharField(max_length=255,null=True)
    no_ext = CharField(max_length=255,null=True)
    no_int = CharField(max_length=255,null=True)
    colonia = CharField(max_length=255,null=True)
    delegacion_municipio = CharField(max_length=255,null=True)
    estado = CharField(max_length=255,null=True)
    correo = CharField(max_length=255,null=True)
    telefono = CharField(max_length=255,null=True)
    movil = CharField(max_length=255,null=True)
    clabe_interbancaria = CharField(max_length=255,null=True)
    contrasena = CharField(max_length=255,null=True)
    id_usuario = IntegerField(null=True)
    ine = CharField(max_length=255,null=True)
    constancia_fiscal = CharField(max_length=255,null=True)
    cuenta_bancaria = CharField(max_length=255,null=True)
    poder_notarial = CharField(max_length=255,null=True)
    acta_constitutiva = CharField(max_length=255,null=True)
    remember_token = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        database = database
        table_name = 'agentes'