from ..Database.database import database 
from peewee import *
from datetime import datetime
from ..Models.Estatus_registro import Estatus_registro

class Usuario(Model):
    correo = CharField(max_length=255,null=True)
    nombre_usuario = CharField(max_length=255,null=True)
    contrasena = CharField(max_length=255,null=True)
    tipo = CharField(max_length=255,null=True)
    estatus_id = ForeignKeyField(Estatus_registro, to_field="id",null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    id:int
    
    def __str__(self):
        return self.nombre_usuario
    
    class Meta:
        database = database
        table_name = 'usuarios'
        