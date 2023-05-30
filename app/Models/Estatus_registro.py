from ..Database.database import database 
from peewee import *
from datetime import datetime

class Estatus_registro(Model):
    estatus = CharField(max_length=255,null=True)
        
    def __str__(self):
        return self.estatus
    
    class Meta:
        database = database
        table_name = 'estatus_registro'
    
    
        