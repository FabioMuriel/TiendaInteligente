class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def aplicar_descuento(self, descuento):
        total = self.calcular_total()
        return total * (1 - descuento)

    def __str__(self):
        return "\n".join(f"{producto.nombre} x {cantidad}" for producto, cantidad in self.productos)