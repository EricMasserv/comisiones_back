from ..Database.database import database 
from peewee import *
from datetime import datetime

class Validador(Model):
    nombre_completo = CharField(max_length=255,null=True)
    correo = CharField(max_length=255,null=True)
    contraseña = CharField(max_length=255,null=True)
    estatus = IntegerField(null=True)
    remember_token = CharField(max_length=255,null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.nombre_validador
    
    class Meta:
        database = database
        table_name = 'validadores'