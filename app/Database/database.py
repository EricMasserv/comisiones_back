from peewee import *

database = MySQLDatabase(
    database ='prueba_python',
    user = 'root',
    password = 'root',
    host = 'localhost',
    port = 3306
)