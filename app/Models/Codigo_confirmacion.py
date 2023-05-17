from ..Database.database import database 
from peewee import *
from datetime import datetime

class Codigo_confirmacion(Model):
    correo_agente = CharField(max_length=255,null=True)
    codigo = CharField(max_length=255,null=True)
    activo = IntegerField(null=True)
    ip = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.ip
    
    class Meta:
        database = database
        table_name = 'codigo_confirmacion'