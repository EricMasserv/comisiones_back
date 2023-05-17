from ..Database.database import database 
from peewee import *
from datetime import datetime

class Venta(Model):
    id_compania = IntegerField(null=True)
    id_division = IntegerField(null=True)
    id_agente = IntegerField(null=True)
    tipo_asistencia = CharField(max_length=255,null=True)
    folio_asistencia = CharField(max_length=255,null=True)
    importe_asistencia = IntegerField(null=True)
    empresa_tipo_comision = CharField(null=True)
    empresa_comision_importe = IntegerField(null=True)
    division_tipo_comision = CharField(null=True)
    division_comision_importe = IntegerField(null=True)
    agente_tipo_comision = CharField(null=True)
    agente_comision_importe = IntegerField(null=True)
    metodo = CharField(max_length=255,null=True)
    estatus = IntegerField(null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.tipo_asistencia
    
    class Meta:
        database = database
        table_name = 'ventas'