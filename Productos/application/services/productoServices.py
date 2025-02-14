from typing import List, Optional
from Productos.domain.entities.productos import Producto
from Productos.domain.interface.productoRepository import ProductoRepositorio

class ProductoService:
    def __init__(self, repositorio: ProductoRepositorio):
        self.repositorio = repositorio

    def crear_producto(self, nombre: str, descripcion: str, precio: float, stock: int, categoria: str) -> Producto:
        """Crea un nuevo producto en la base de datos."""
        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria
        )
        self.repositorio.crear(nuevo_producto)
        return nuevo_producto

    def buscar_por_id(self, id: int) -> Optional[Producto]:
        """Busca un producto por su ID."""
        return self.repositorio.buscar_por_id(id)

    def listar_por_categoria(self, categoria: str) -> List[Producto]:
        """Lista todos los productos de una categoría específica."""
        return self.repositorio.listar(categoria)

    def editar_producto(self, id: int, nombre: str, descripcion: str, precio: float, stock: int, categoria: str) -> Optional[Producto]:
        """Edita un producto existente en la base de datos."""
        producto_existente = self.repositorio.buscar_por_id(id)
        if not producto_existente:
            return None  # Producto no encontrado

        # Actualizar valores
        producto_existente.nombre = nombre
        producto_existente.descripcion = descripcion
        producto_existente.precio = precio
        producto_existente.stock = stock
        producto_existente.categoria = categoria

        self.repositorio.editar(id, producto_existente)
        return producto_existente

    def eliminar_producto(self, id: int) -> bool:
        """Elimina un producto por su ID."""
        producto_existente = self.repositorio.buscar_por_id(id)
        if not producto_existente:
            return False  # Producto no encontrado

        return self.repositorio.eliminar(id)
