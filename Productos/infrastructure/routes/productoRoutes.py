from flask import Blueprint, request, jsonify
from Productos.application.services.productoServices import ProductoService
from Productos.infrastructure.repositories.productoRepostoryMysql import ProductoRepositorioMySQL

producto_router = Blueprint("productos", __name__)
servicio = ProductoService(ProductoRepositorioMySQL())

@producto_router.route("/productos", methods=["POST"])
def crear_producto():
    datos = request.json
    nuevo_producto = servicio.crear_producto(
        nombre=datos["nombre"],
        descripcion=datos["descripcion"],
        precio=datos["precio"],
        stock=datos["stock"],
        categoria=datos["categoria"]
    )
    return jsonify({"message": "Producto creado", "producto": nuevo_producto.__dict__}), 201

@producto_router.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    producto = servicio.buscar_por_id(id)
    
    # Si producto es un diccionario, lo devuelves directamente
    return jsonify(producto) if producto else jsonify({"error": "Producto no encontrado"}), 404


@producto_router.route('/categoria/<categoria>', methods=['GET'])
def listar_por_categoria(categoria):
    productos = servicio.listar_por_categoria(categoria)
    
    if productos:
        # Convertir la lista de productos en un formato adecuado para JSON
        productos_json = [producto.__dict__ for producto in productos]
        return jsonify(productos_json)
    else:
        return jsonify([]), 200

@producto_router.route("/productos/<int:id>", methods=["PUT"])
def editar_producto(id):
    datos = request.json
    producto_editado = servicio.editar_producto(
        id=id,
        nombre=datos["nombre"],
        descripcion=datos["descripcion"],
        precio=datos["precio"],
        stock=datos["stock"],
        categoria=datos["categoria"]
    )
    return jsonify({"message": "Producto actualizado", "producto": producto_editado.__dict__}) if producto_editado else jsonify({"error": "Producto no encontrado"}), 404

@producto_router.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    eliminado = servicio.eliminar_producto(id)
    return jsonify({"message": "Producto eliminado"}) if eliminado else jsonify({"error": "Producto no encontrado"}), 404
