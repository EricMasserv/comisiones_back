from fastapi import FastAPI
from fastapi import HTTPException
from .Models.Compania import Compania
from .Models.Division import Division
from .Models.Agente import Agente
from .Models.Validador import Validador
from .Models.Expediente import Expediente
from .Models.Producto import Producto
from .Models.Tipo_archivo import Tipo_archivo
from .Models.Venta import Venta
from .Models.Regimenes_fiscales import Regimenes_fiscales
from .Models.Boveda import Boveda
from .Models.Centro_costo import Centro_costo
from .Models.Codigo_confirmacion import Codigo_confirmacion
from .Models.Usuario import Usuario
from .Database.database import database as connection

from fastapi.middleware.cors import CORSMiddleware
from .routers import compania
from .routers import division
from .routers import agente
from .routers import validador
from .routers import expediente
from .routers import producto
from .routers import tipo_archivo
from .routers import venta
from .routers import regimenes_fiscales
from .routers import boveda
from .routers import centro_costo
from .routers import codigo_confirmacion
from .routers import auth
from .routers import login

app = FastAPI (title =  'Comisiones Escalonadas',
               descripcion = 'comisiones escalonadas con python',
               version = '0.0.0.1')


origins = [
"*",
]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

app.include_router(compania.compania_router)
app.include_router(division.division_router)
app.include_router(agente.agente_router)
app.include_router(validador.validador_router)
app.include_router(expediente.expediente_router)
app.include_router(producto.producto_router)
app.include_router(tipo_archivo.tipo_archivo_router)
app.include_router(venta.venta_router)
app.include_router(regimenes_fiscales.regimenes_fiscales)
app.include_router(boveda.boveda)
app.include_router(centro_costo.centro_costo)
app.include_router(codigo_confirmacion.codigo_confirmacion)
app.include_router(auth.usuario)
app.include_router(login.login)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()  
        connection.create_tables([Compania, Division, Agente, Validador, Expediente, Producto, Tipo_archivo, Venta, Regimenes_fiscales, Boveda, Centro_costo, Codigo_confirmacion, Usuario])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        