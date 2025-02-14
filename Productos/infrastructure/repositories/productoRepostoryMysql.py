from typing import List, Optional
from Productos.domain.entities.productos import Producto
from Productos.domain.interface.productoRepository import ProductoRepositorio
from Productos.infrastructure.database.conexion import Conexion


class ProductoRepositorioMySQL:
    def __init__(self):
        # Obtiene una conexión real a la base de datos usando la clase Conexion
        self.db = Conexion.obtener_conexion()
        self.cursor = self.db.cursor(dictionary=True)

    def crear(self, producto):
        try:
            query = """
            INSERT INTO productos (nombre, descripcion, precio, stock, categoria)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria)
            self.cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"Error al crear producto: {e}")

    def buscar_por_id(self, id: int):
        try:
            query = "SELECT * FROM productos WHERE id = %s"
            self.cursor.execute(query, (id,))
            resultado = self.cursor.fetchone()
            return resultado  # Retorna un diccionario con los datos del producto
        except Exception as e:
            print(f"Error al buscar producto por ID: {e}")
            return None

    def editar(self, id: int, producto):
        try:
            query = """
            UPDATE productos
            SET nombre = %s, descripcion = %s, precio = %s, stock = %s, categoria = %s
            WHERE id = %s
            """
            values = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.categoria, id)
            self.cursor.execute(query, values)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"Error al editar producto: {e}")

class ProductoRepositorioMySQL:
    def __init__(self):
        self.db = Conexion.obtener_conexion()
        self.cursor = self.db.cursor(dictionary=True)

    def listar(self, categoria):
        try:
            query = "SELECT * FROM productos WHERE categoria = %s"
            self.cursor.execute(query, (categoria,))
            resultados = self.cursor.fetchall()
            
            productos = []
            for fila in resultados:
                # Aquí creamos el objeto Producto
                producto = Producto(
                    id=fila['id'],  # Este es el id de la base de datos
                    nombre=fila['nombre'],
                    descripcion=fila['descripcion'],
                    precio=fila['precio'],
                    stock=fila['stock'],
                    categoria=fila['categoria'],
                    created_at=fila['created_at']
                )
                productos.append(producto)
            
            return productos
        
        except Exception as e:
            print(f"Error al listar productos: {e}")
            return []

