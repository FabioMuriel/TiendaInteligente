from models.carrito import Carrito

class CarritoService:
    def __init__(self):
        self.carrito = Carrito()

    def agregar_producto(self, producto, cantidad):
        self.carrito.agregar_producto(producto, cantidad)

    def calcular_total(self):
        return self.carrito.calcular_total()

    def aplicar_descuento(self, descuento):
        return self.carrito.aplicar_descuento(descuento)

    def obtener_productos(self):
        return self.carrito.productos