from typing import Optional

class Producto:
    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int, categoria: str, id: Optional[int] = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
