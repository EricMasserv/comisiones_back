from fastapi import APIRouter
from fastapi import HTTPException
from ..Models.Producto import Producto
from ..Schemas.ProductoCreateModel import ProductoCreateRequestModel, ProductoResponseModel
from ..Schemas.ProductoUpdateModel import ProductoUpdateRequestModel, ProductoUpdateResponseModel

producto_router = APIRouter(
    prefix = "/producto",
    tags = ["Producto"]
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
                             Producto.nombre_division:producto_request.nombre_division,
                             Producto.regimen_fiscal_id:producto_request.regimen_fiscal_id,
                             Producto.rfc:producto_request.rfc,
                             Producto.correo:producto_request.correo,
                             Producto.telefono:producto_request.telefono,
                             Producto.comision_porcentaje:producto_request.comision_porcentaje,
                             Producto.comision_fija:producto_request.comision_fija,
                             Producto.tipo_pago:producto_request.tipo_pago,
                             Producto.dia_maximo_pago_reclamo:producto_request.dia_maximo_pago_reclamo,
                             Producto.dia_pago:producto_request.dia_pago,
                             Producto.fecha_corte:producto_request.fecha_corte,
                             Producto.banco_nombre:producto_request.banco_nombre,
                             Producto.banco_numero_cuenta:producto_request.banco_numero_cuenta,
                             Producto.banco_clabe_bancaria:producto_request.banco_clabe_bancaria,
                             Producto.banco_codigo_swift:producto_request.banco_codigo_swift,
                             Producto.banco_codigo_iban:producto_request.banco_codigo_iban,
                             Producto.banco_codigo_bic:producto_request.banco_codigo_bic,
                             Producto.banco_domicilio:producto_request.banco_domicilio,
                             Producto.tipo_moneda:producto_request.tipo_moneda,
                             Producto.contraseña:producto_request.contraseña,
                             Producto.direccion:producto_request.direccion,
                             Producto.estatus:producto_request.estatus
                             }).where(Producto.id == producto_request.id)
        qry.execute()
                   
        return {'Producto actualizado'}
    else:
        return HTTPException(404, 'Producto no encontrado')