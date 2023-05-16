from ..Database.database import database 
from peewee import *
from datetime import datetime

class Expediente(Model):
    id_compania = IntegerField(null=True)
    id_division = IntegerField(null=True)
    id_agente = IntegerField(null=True)
    id_tipo_archivo = IntegerField(null=True)
    ruta = CharField(max_length=255,null=True)
    estatus = IntegerField(null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.id_tipo_archivo
    
    class Meta:
        database = database
        table_name = 'expedientes'