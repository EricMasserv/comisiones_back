from fastapi import APIRouter
from fastapi import HTTPException
from ...Models.Producto import Producto
from ...Schemas.Producto.ProductoCreateModel import ProductoCreateRequestModel, ProductoResponseModel
from ...Schemas.Producto.ProductoUpdateModel import ProductoUpdateRequestModel, ProductoUpdateResponseModel
from ...Middlewares.verify_token_route import VerifyTokenRoute

producto_router = APIRouter(
    prefix = "/producto",
    tags = ["Producto"],
    route_class=VerifyTokenRoute
)

@producto_router.post('/create')
async def create_producto(producto_request: ProductoCreateRequestModel):
    producto = Producto.create(
        id_compania=producto_request.id_compania,
        id_compania_mass=producto_request.id_compania_mass,
        id_plan_mass=producto_request.id_plan_mass,
        nombre=producto_request.nombre,
        precio=producto_request.precio,
        comision_porcentaje=producto_request.comision_porcentaje,
        comision_fija=producto_request.comision_fija,
        limite_superior=producto_request.limite_superior,
        limite_inferior=producto_request.limite_inferior,
        estatus=producto_request.estatus
    )
    
    return producto_request

@producto_router.get('/show/{producto_id}')
async def get_producto(producto_id):
    producto = Producto.select().where(Producto.id == producto_id).first()
    if  producto:
        return ProductoResponseModel(id=producto.id,
                                    id_compania=producto.id_compania,
                                    id_compania_mass=producto.id_compania_mass,
                                    id_plan_mass=producto.id_plan_mass,
                                    nombre=producto.nombre,
                                    precio=producto.precio,
                                    comision_porcentaje=producto.comision_porcentaje,
                                    comision_fija=producto.comision_fija,
                                    limite_superior=producto.limite_superior,
                                    limite_inferior=producto.limite_inferior,
                                    estatus=producto.estatus
                                 )
    else:
        return HTTPException(404, 'Producto no encontrado')

@producto_router.get('/show_all')
async def get_producto_all():
    return list(Producto.select().dicts());
    
@producto_router.get('/delete/{producto_id}')
async def delete_producto(producto_id):
    producto = Producto.select().where(Producto.id == producto_id).first()
    if  producto:
        producto.delete_instance()
        return {'Producto eliminado'}
    else:
        return HTTPException(404, 'Producto not found')
    
@producto_router.post('/update/')
async def update_producto(producto_request: ProductoUpdateRequestModel):
    producto = Producto.select().where(Producto.id == producto_request.id).first()
    if producto:     
               
        qry=Producto.update({Producto.id_compania:producto_request.id_compania,
                             Producto.id_compania_mass:producto_request.id_compania_mass,
                             Producto.id_plan_mass:producto_request.id_plan_mass,
                             Producto.nombre:producto_request.nombre,
                             Producto.precio:producto_request.precio,
                             Producto.comision_porcentaje:producto_request.comision_porcentaje,
                             Producto.comision_fija:producto_request.comision_fija,
                             Producto.limite_superior:producto_request.limite_superior,
                             Producto.limite_inferior:producto_request.limite_inferior,
                             Producto.estatus:producto_request.estatus
                             }).where(Producto.id == producto_request.id)
        qry.execute()
                   
        return {'Producto actualizado'}
    else:
        return HTTPException(404, 'Producto no encontrado')