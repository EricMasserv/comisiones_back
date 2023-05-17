from ..Database.database import database 
from peewee import *
from datetime import datetime

class Regimenes_fiscales(Model):
    codigo = CharField(max_length=255,null=True)
    nombre = CharField(max_length=255,null=True)
    descripcion = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        database = database
        table_name = 'regimenes_fiscales'