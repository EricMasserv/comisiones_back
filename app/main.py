from fastapi import FastAPI
from fastapi import HTTPException
from .Models.Company import Company
from .Models.Division import Division
from .Database.database import database as connection

from fastapi.middleware.cors import CORSMiddleware
from .routers import company
from .routers import division

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

app.include_router(company.company_router)
app.include_router(division.division_router)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()  
        connection.create_tables([Company, Division])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        