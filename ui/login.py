from tkinter import *
from tkinter import messagebox
from services.usuario_service import UsuarioService
from ui.gui import TiendaApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        self.usuario_service = UsuarioService()

        # Estilos
        self.font = ("Helvetica", 12)
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.text_color = "#333333"

        self.root.configure(bg=self.bg_color)

        # Interfaz de login
        self.label_email = Label(root, text="Email:", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.label_email.grid(row=0, column=0, padx=10, pady=10)
        self.entry_email = Entry(root, font=self.font)
        self.entry_email.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = Label(root, text="Contraseña:", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password = Entry(root, font=self.font, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.boton_login = Button(root, text="Iniciar Sesión", font=self.font, bg=self.button_color, fg="white", command=self.iniciar_sesion)
        self.boton_login.grid(row=2, column=0, columnspan=2, pady=10)

        self.boton_registro = Button(root, text="Registrarse", font=self.font, bg=self.button_color, fg="white", command=self.mostrar_registro)
        self.boton_registro.grid(row=3, column=0, columnspan=2, pady=10)

    def iniciar_sesion(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        usuario = self.usuario_service.autenticar_usuario(email, password)
        if usuario:
            messagebox.showinfo("Login Exitoso", f"Bienvenido, {usuario.nombre}!")
            self.root.destroy()  # Cerrar la ventana de login
            self.abrir_tienda()  # Abrir la ventana principal de la tienda
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos")

    def mostrar_registro(self):
        registro_window = Toplevel(self.root)
        registro_window.title("Registro")
        registro_window.geometry("300x200")

        Label(registro_window, text="Nombre:", font=self.font).grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = Entry(registro_window, font=self.font)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        Label(registro_window, text="Email:", font=self.font).grid(row=1, column=0, padx=10, pady=10)
        entry_email = Entry(registro_window, font=self.font)
        entry_email.grid(row=1, column=1, padx=10, pady=10)

        Label(registro_window, text="Contraseña:", font=self.font).grid(row=2, column=0, padx=10, pady=10)
        entry_password = Entry(registro_window, font=self.font, show="*")
        entry_password.grid(row=2, column=1, padx=10, pady=10)

        Button(registro_window, text="Registrarse", font=self.font, bg=self.button_color, fg="white", command=lambda: self.registrar_usuario(entry_nombre.get(), entry_email.get(), entry_password.get(), registro_window)).grid(row=3, column=0, columnspan=2, pady=10)

    def registrar_usuario(self, nombre, email, password, ventana):
        if not nombre or not email or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            self.usuario_service.registrar_usuario(nombre, email, password)
            messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente")
            ventana.destroy()  # Cerrar la ventana de registro
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el usuario: {str(e)}")

    def abrir_tienda(self):
        root = Tk()
        app = TiendaApp(root)
        root.mainloop()