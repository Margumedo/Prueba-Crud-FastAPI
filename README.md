![](https://camo.githubusercontent.com/86d9ca3437f5034da052cf0fd398299292aab0e4479b58c20f2fc37dd8ccbe05/68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67)

# FastAPI CRUD prueba with SQLAlchemy, Alembic and PostgreSQL

Crear una API CRUD de usuarios y productos en Python con ORM utilizando las librerías FastAPI y SQLAlchemy.

El ORM de la API debe de tener modelos para almacenar tanto el nombre y precio de los productos como el nombre y dirección de correo de los usuarios. También se debe poder almacenar los productos que un usuario ha comprado y los pedidos que este ha hecho.

La API debe contar con endpoints para:

- Agregar un nuevo usuario. ✅

- Obtener una lista de todos los usuarios. ✅

- Agregar un nuevo producto. ✅

- Obtener una lista de todos los productos. ✅

- Obtener todos los productos que ha comprado un usuario ✅

- Obtener todos los usuarios que han comprado un producto ✅

- Obtener todos los productos de un pedido. ✅

- Eliminar un producto. ✅

- Actualizar los datos de un producto. ✅

Puede usarse cualquier variación de SQL (como Postgres o MySQL) para la base de datos. Lo importante es la capacidad de la API para conectarse a esta.

###Blockquotes

> Recuerda crear y activar tu entorno virtual antes de instalar los requerimientos.

## Setup

1. **Installation of Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

# Database Setup

Instalar PostgreSQL y arrancar el servidor de la base de datos. Crear una nueva base de datos PostgreSQL. Copiar `.env.example` a `.env` y llenar los valores de la variable de entorno de la URL de conexión a la base de datos y otros valores necesarios.

# Running the Application

Executar la aplicación con `uvicorn main:app --reload`:

```bash
 uvicorn main:app --reload
```

La API estará disponible en http://127.0.0.1:8000.

# API Endpoints

## Users

Create: `POST /users/`

Read:

- `GET /users/`
- `GET /users/{user_id}`

Update: `PATCH /users/{user_id}`

Delete: `DELETE /users/{user_id}`

## Products

Create: `POST /products/`

Read:

- `GET /products/`
- `GET /products/{product_id}`

Update: `PUT /products/{product_id}`

Delete: `DELETE /products/{product_id}`

## Orders

Create: `POST /orders/`

# Testing

Utilizar herramientas como curl o Postman para probar las solicitudes API. También se pueden agregar pruebas unitarias con pytest.

# Deployment

Considerar el uso de servidores ASGI como Uvicorn o Hypercorn detrás de un proxy inverso como Nginx o Apache.
