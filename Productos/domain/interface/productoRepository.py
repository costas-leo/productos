from abc import ABC, abstractmethod
from typing import List, Optional
from Productos.domain.entities.productos import Producto 
class ProductoRepositorio(ABC):  

    @abstractmethod
    def crear(self, producto: Producto) -> None:
        """Guarda un nuevo producto en la base de datos"""
        pass

    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[Producto]:
        """Busca un producto por su ID"""
        pass

    @abstractmethod
    def editar(self, id: int, producto: Producto) -> None:
        """Edita un producto existente"""
        pass

    @abstractmethod
    def listar(self, categoria: str) -> List[Producto]:
        """Lista productos por categoría"""
        pass
