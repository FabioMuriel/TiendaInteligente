# utils/receipt.py
from datetime import datetime

def generar_datos_recibo(carrito, descuento, total_con_descuento):
    # Datos del recibo
    recibo = {
        "fecha": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "productos": [],
        "total": sum(producto.precio * cantidad for producto, cantidad in carrito),
        "descuento": descuento * 100,
        "total_con_descuento": total_con_descuento,
    }

    # Agregar productos al recibo
    for producto, cantidad in carrito:
        recibo["productos"].append({
            "nombre": producto.nombre,
            "cantidad": cantidad,
            "precio_unitario": producto.precio,
            "subtotal": producto.precio * cantidad,
        })

    return recibo