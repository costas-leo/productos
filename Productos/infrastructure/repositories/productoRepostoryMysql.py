from typing import List, Optional
from Productos.domain.entities.productos import Producto
from Productos.domain.interface.productoRepository import ProductoRepositorio
from Productos.infrastructure.database.conexion import Conexion


class ProductoRepositorioMySQL(ProductoRepositorio):

    def crear(self, producto: Producto) -> None:
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO productos (nombre, descripcion, precio, stock, categoria) VALUES (%s, %s, %s, %s, %s)"
        valores = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    def buscar_por_id(self, id: int) -> Optional[Producto]:
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM productos WHERE id = %s"
        cursor.execute(query, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()

        if resultado:
            return Producto(
                id=resultado["id"],
                nombre=resultado["nombre"],
                descripcion=resultado["descripcion"],
                precio=resultado["precio"],
                stock=resultado["stock"],
                categoria=resultado["categoria"]
            )
        return None

    def editar(self, id: int, producto: Producto) -> None:
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        query = "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s, categoria=%s WHERE id=%s"
        valores = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria, id)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    def listar(self, categoria: str) -> List[Producto]:
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM productos WHERE categoria = %s"
        cursor.execute(query, (categoria,))
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()

        return [Producto(
            id=row["id"],
            nombre=row["nombre"],
            descripcion=row["descripcion"],
            precio=row["precio"],
            stock=row["stock"],
            categoria=row["categoria"]
        ) for row in resultados]

    def eliminar(self, id: int) -> bool:
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas_afectadas > 0