from ..Database.database import database 
from peewee import *
from datetime import datetime

class Usuario(Model):
    correo = CharField(max_length=255,null=True)
    contrasena = CharField(max_length=255,null=True)
    tipo = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.correo
    
    class Meta:
        database = database
        table_name = 'usuarios'