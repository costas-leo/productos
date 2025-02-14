from flask import Blueprint, request, jsonify
from Productos.application.services.productoServices import ProductoService
from Productos.infrastructure.repositories.productoRepostoryMysql import ProductoRepositorioMySQL

producto_router = Blueprint("producto_router", __name__)
repositorio = ProductoRepositorioMySQL()
servicio = ProductoService(repositorio)

@producto_router.route("/productos", methods=["POST"])
def crear_producto():
    data = request.json
    nuevo_producto = servicio.crear_producto(
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=data["precio"],
        stock=data["stock"],
        categoria=data["categoria"]
    )
    return jsonify({"mensaje": "Producto creado", "producto": nuevo_producto.__dict__}), 201

@producto_router.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    producto = servicio.buscar_por_id(id)
    if producto:
        return jsonify(producto.__dict__)
    return jsonify({"error": "Producto no encontrado"}), 404

@producto_router.route("/productos/categoria/<string:categoria>", methods=["GET"])
def listar_productos(categoria):
    productos = servicio.listar_por_categoria(categoria)
    return jsonify([p.__dict__ for p in productos])

@producto_router.route("/productos/<int:id>", methods=["PUT"])
def editar_producto(id):
    data = request.json
    producto_actualizado = servicio.editar_producto(
        id=id,
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=data["precio"],
        stock=data["stock"],
        categoria=data["categoria"]
    )
    if producto_actualizado:
        return jsonify({"mensaje": "Producto actualizado", "producto": producto_actualizado.__dict__})
    return jsonify({"error": "Producto no encontrado"}), 404

@producto_router.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    if servicio.eliminar_producto(id):
        return jsonify({"mensaje": "Producto eliminado"})
    return jsonify({"error": "Producto no encontrado"}), 404