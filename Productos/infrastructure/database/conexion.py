import mysql.connector

class Conexion:
    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            database='inventario_productos'
        )
