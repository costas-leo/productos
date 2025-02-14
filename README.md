# Proyecto de Productos

## Tabla de contenidos

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Cómo usarlo](#cómo-usarlo)
- [Rutas de la API](#rutas-de-la-api)

---

## Introducción

Este proyecto es una aplicación backend diseñada para la gestión de productos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los productos, categorizarlos y administrar su stock.

El programa expone una API REST utilizando **Flask** para manejar las operaciones y es compatible con herramientas como **Postman** para realizar pruebas y simulaciones de solicitudes. La base de datos utilizada es **MySQL**.

---

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd productos-backend
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install  mysql-connector-python
   pip install flask 
   ```

3. Configura la base de datos en `Conexion`:

   ```python
   import mysql.connector

   class Conexion:
       @staticmethod
       def obtener_conexion():
           return mysql.connector.connect(
               host='localhost',
               user='root',
               database='inventario_productos'
           )
   ```

---

## Cómo usarlo

Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
python app.py
```

La API estará disponible en `http://127.0.0.1:5000`.

### Ejemplo de uso con Postman

- **Crear un producto:**

  - Ruta: `POST /productos`
  - Body (JSON):
    ```json
    {
        "nombre": "Producto A",
        "descripcion": "Descripcion del producto",
        "precio": 100.5,
        "stock": 50,
        "categoria": "Electrónica"
    }
    ```

- **Leer un producto por ID:**

  - Ruta: `GET /productos/<id>`

- **Actualizar un producto:**

  - Ruta: `PUT /productos/<id>`
  - Body (JSON):
    ```json
    {
        "nombre": "Producto B",
        "descripcion": "Nueva descripcion",
        "precio": 150.0,
        "stock": 30,
        "categoria": "Hogar"
    }
    ```

- **Eliminar un producto:**

  - Ruta: `DELETE /productos/<id>`

---

## Rutas de la API

### Productos

- **Crear producto**: `POST /productos`
- **Leer producto por ID**: `GET /productos/<id>`
- **Actualizar producto**: `PUT /productos/<id>`
- **Eliminar producto**: `DELETE /productos/<id>`
- **Obtener productos por categoría**: `GET /productos/categoria/<categoria>`

---

