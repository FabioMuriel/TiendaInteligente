# services/producto_service.py
from models.producto import Producto
from database.database import Database

class ProductoService:
    def __init__(self):
        self.db = Database("tienda_inteligente.db")

    def crear_producto(self, nombre, precio):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        producto_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Producto(producto_id, nombre, precio)

    def obtener_productos(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()
        return [Producto(id, nombre, precio) for id, nombre, precio in productos]