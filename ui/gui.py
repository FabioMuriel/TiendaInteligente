# ui/gui.py
from tkinter import *
from tkinter import messagebox
from services.carrito_service import CarritoService
from services.producto_service import ProductoService
from utils.receipt import generar_datos_recibo

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mercado Inteligente")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        self.carrito_service = CarritoService()
        self.producto_service = ProductoService()

        self.font = ("Helvetica", 12)
        self.bg_color = "#34495e" 
        self.button_color = "#1abc9c"
        self.text_color = "#ecf0f1"  
        self.accent_color = "#3498db"

        self.main_frame = Frame(root, bg=self.bg_color, padx=20, pady=20)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.label_titulo = Label(
            self.main_frame,
            text="Mercado Inteligente",
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Campo de nombre del producto
        self.label_nombre = Label(
            self.main_frame,
            text="Nombre del Producto:",
            font=self.font,
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_nombre = Entry(self.main_frame, font=self.font, bd=2, relief=FLAT)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

        # Campo de precio (solo números)
        self.label_precio = Label(
            self.main_frame,
            text="Precio Unitario:",
            font=self.font,
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_precio.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        # Validación para el campo de precio
        validacion_precio = self.main_frame.register(self.validar_numeros)  # Registrar la función de validación
        self.entry_precio = Entry(
            self.main_frame,
            font=self.font,
            bd=2,
            relief=FLAT,
            validate="key",  # Validar en cada tecla presionada
            validatecommand=(validacion_precio, "%P")  # Pasar el texto futuro (%P) a la función
        )
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

        # Campo de cantidad (solo números enteros)
        self.label_cantidad = Label(
            self.main_frame,
            text="Cantidad:",
            font=self.font,
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_cantidad.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        # Validación para el campo de cantidad
        validacion_cantidad = self.main_frame.register(self.validar_enteros)  # Registrar la función de validación
        self.entry_cantidad = Entry(
            self.main_frame,
            font=self.font,
            bd=2,
            relief=FLAT,
            validate="key",  # Validar en cada tecla presionada
            validatecommand=(validacion_cantidad, "%P")  # Pasar el texto futuro (%P) a la función
        )
        self.entry_cantidad.grid(row=3, column=1, padx=10, pady=10, sticky=EW)

        # Botón de agregar al carrito
        self.boton_agregar = Button(
            self.main_frame,
            text="Agregar al Carrito",
            font=self.font,
            bg=self.button_color,
            fg="white",
            bd=0,
            relief=FLAT,
            padx=20,
            pady=10,
            command=self.agregar_al_carrito,
        )
        self.boton_agregar.grid(row=4, column=0, columnspan=2, pady=10, sticky=EW)

        # Botón de finalizar compra
        self.boton_finalizar = Button(
            self.main_frame,
            text="Finalizar Compra",
            font=self.font,
            bg=self.accent_color,
            fg="white",
            bd=0,
            relief=FLAT,
            padx=20,
            pady=10,
            command=self.finalizar_compra,
        )
        self.boton_finalizar.grid(row=5, column=0, columnspan=2, pady=10, sticky=EW)

        # Área del carrito
        self.label_carrito = Label(
            self.main_frame,
            text="Carrito de Compras",
            font=("Helvetica", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_carrito.grid(row=6, column=0, columnspan=2, pady=(20, 10))

        self.texto_carrito = Text(
            self.main_frame,
            height=10,
            width=50,
            font=self.font,
            bg="white",
            fg="#333333", 
            bd=2,
            relief=FLAT,
        )
        self.texto_carrito.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky=EW)

        self.main_frame.grid_columnconfigure(1, weight=1)

    def agregar_al_carrito(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()

        # Validar que los campos no estén vacíos
        if not nombre or not precio or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Convertir a números
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números válidos")
            return

        # Agregar producto al carrito
        producto = self.producto_service.crear_producto(nombre, precio)
        self.carrito_service.agregar_producto(producto, cantidad)

        self.texto_carrito.insert(END, f"{producto.nombre} x {cantidad}\n")

    def finalizar_compra(self):
        productos = self.carrito_service.obtener_productos()
        total = self.carrito_service.calcular_total()
        descuento = 0.1 if len(productos) >= 3 else 0
        total_con_descuento = self.carrito_service.aplicar_descuento(descuento)

        recibo = generar_datos_recibo(productos, descuento, total_con_descuento)
        self.mostrar_recibo(recibo)

    def mostrar_recibo(self, recibo):
        recibo_window = Toplevel(self.root)
        recibo_window.title("Recibo de Compra")
        recibo_window.geometry("500x400")
        recibo_window.configure(bg="#2c3e50")

        recibo_frame = Frame(recibo_window, bg="#34495e", padx=20, pady=20)
        recibo_frame.pack(fill=BOTH, expand=True)

        label_titulo = Label(
            recibo_frame,
            text="Recibo de Compra",
            font=("Helvetica", 18, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
        )
        label_titulo.pack(pady=10)

        label_fecha = Label(
            recibo_frame,
            text=f"Fecha: {recibo['fecha']}",
            font=("Helvetica", 12),
            bg="#34495e",
            fg="#ecf0f1",
        )
        label_fecha.pack(pady=5)

        frame_tabla = Frame(recibo_frame, bg="#34495e")
        frame_tabla.pack(pady=10)

        Label(frame_tabla, text="Producto", font=("Helvetica", 12, "bold"), bg="#34495e", fg="#ecf0f1").grid(row=0, column=0, padx=10, pady=5)
        Label(frame_tabla, text="Cantidad", font=("Helvetica", 12, "bold"), bg="#34495e", fg="#ecf0f1").grid(row=0, column=1, padx=10, pady=5)
        Label(frame_tabla, text="Precio Unitario", font=("Helvetica", 12, "bold"), bg="#34495e", fg="#ecf0f1").grid(row=0, column=2, padx=10, pady=5)
        Label(frame_tabla, text="Subtotal", font=("Helvetica", 12, "bold"), bg="#34495e", fg="#ecf0f1").grid(row=0, column=3, padx=10, pady=5)

        for i, producto in enumerate(recibo["productos"], start=1):
            Label(frame_tabla, text=producto["nombre"], font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").grid(row=i, column=0, padx=10, pady=5)
            Label(frame_tabla, text=producto["cantidad"], font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").grid(row=i, column=1, padx=10, pady=5)
            Label(frame_tabla, text=f"${producto['precio_unitario']:.2f}", font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").grid(row=i, column=2, padx=10, pady=5)
            Label(frame_tabla, text=f"${producto['subtotal']:.2f}", font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").grid(row=i, column=3, padx=10, pady=5)

        Label(recibo_frame, text=f"Total: ${recibo['total']:.2f}", font=("Helvetica", 12, "bold"), bg="#34495e", fg="#ecf0f1").pack(pady=5)
        Label(recibo_frame, text=f"Descuento ({recibo['descuento']:.0f}%): ${recibo['total'] * (recibo['descuento'] / 100):.2f}", font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").pack(pady=5)
        Label(recibo_frame, text=f"Total a pagar: ${recibo['total_con_descuento']:.2f}", font=("Helvetica", 12, "bold"), bg="#34495e", fg="#1abc9c").pack(pady=10)

    def validar_numeros(self, texto_futuro):
        # Permitir solo números y un punto decimal
        if texto_futuro == "":  # Permitir campo vacío
            return True
        try:
            float(texto_futuro)  # Intentar convertir a float
            return True
        except ValueError:
            return False  # No es un número válido

    def validar_enteros(self, texto_futuro):
        # Permitir solo números enteros
        if texto_futuro == "":  # Permitir campo vacío
            return True
        return texto_futuro.isdigit()  # Solo dígitos enteros