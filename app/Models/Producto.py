from ..Database.database import database 
from peewee import *
from datetime import datetime

class Producto(Model):
    id_compania = IntegerField(null=True)
    id_compania_mass = IntegerField(null=True)
    id_plan_mass = IntegerField(null=True)
    nombre = CharField(max_length=255,null=True)
    precio = IntegerField(null=True)
    comision_porcentaje = IntegerField(null=True)
    comision_fija = IntegerField(null=True)
    limite_superior = IntegerField(null=True)
    limite_inferior = IntegerField(null=True)
    estatus = IntegerField(null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        database = database
        table_name = 'productos'