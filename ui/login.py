from tkinter import *
from tkinter import messagebox
from services.usuario_service import UsuarioService
from ui.gui import TiendaApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Mercado Inteligente")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")
        self.usuario_service = UsuarioService()

        self.font = ("Helvetica", 12)
        self.bg_color = "#34495e" 
        self.button_color = "#1abc9c"
        self.text_color = "#ecf0f1"  
        self.accent_color = "#3498db"  

        self.main_frame = Frame(root, bg=self.bg_color, padx=20, pady=20)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.label_titulo = Label(
            self.main_frame,
            text="Iniciar Sesión",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.label_email = Label(
            self.main_frame,
            text="Email:",
            font=self.font,
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_email.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_email = Entry(self.main_frame, font=self.font, bd=2, relief=FLAT)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

        self.label_password = Label(
            self.main_frame,
            text="Contraseña:",
            font=self.font,
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.label_password.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.entry_password = Entry(self.main_frame, font=self.font, show="*", bd=2, relief=FLAT)
        self.entry_password.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

        self.boton_login = Button(
            self.main_frame,
            text="Iniciar Sesión",
            font=self.font,
            bg=self.button_color,
            fg="white",
            bd=0,
            relief=FLAT,
            padx=20,
            pady=10,
            command=self.iniciar_sesion,
        )
        self.boton_login.grid(row=3, column=0, columnspan=2, pady=10, sticky=EW)

        self.boton_registro = Button(
            self.main_frame,
            text="Registrarse",
            font=self.font,
            bg=self.accent_color,
            fg="white",
            bd=0,
            relief=FLAT,
            padx=20,
            pady=10,
            command=self.mostrar_registro,
        )
        self.boton_registro.grid(row=4, column=0, columnspan=2, pady=10, sticky=EW)

        self.main_frame.grid_columnconfigure(1, weight=1)

    def iniciar_sesion(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        usuario = self.usuario_service.autenticar_usuario(email, password)
        if usuario:
            messagebox.showinfo("Login Exitoso", f"Bienvenido, {usuario.nombre}!")
            self.root.destroy() 
            self.abrir_tienda() 
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos")

    def mostrar_registro(self):
        registro_window = Toplevel(self.root)
        registro_window.title("Registro - Mercado Inteligente")
        registro_window.geometry("400x300")
        registro_window.configure(bg="#2c3e50")

        registro_frame = Frame(registro_window, bg=self.bg_color, padx=20, pady=20)
        registro_frame.pack(fill=BOTH, expand=True)

        label_titulo_registro = Label(
            registro_frame,
            text="Registro",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
        )
        label_titulo_registro.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        Label(registro_frame, text="Nombre:", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        entry_nombre = Entry(registro_frame, font=self.font, bd=2, relief=FLAT)
        entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

        Label(registro_frame, text="Email:", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        entry_email = Entry(registro_frame, font=self.font, bd=2, relief=FLAT)
        entry_email.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

        Label(registro_frame, text="Contraseña:", font=self.font, bg=self.bg_color, fg=self.text_color).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        entry_password = Entry(registro_frame, font=self.font, show="*", bd=2, relief=FLAT)
        entry_password.grid(row=3, column=1, padx=10, pady=10, sticky=EW)

        Button(
            registro_frame,
            text="Registrarse",
            font=self.font,
            bg=self.button_color,
            fg="white",
            bd=0,
            relief=FLAT,
            padx=20,
            pady=10,
            command=lambda: self.registrar_usuario(entry_nombre.get(), entry_email.get(), entry_password.get(), registro_window),
        ).grid(row=4, column=0, columnspan=2, pady=10, sticky=EW)

        registro_frame.grid_columnconfigure(1, weight=1)

    def registrar_usuario(self, nombre, email, password, ventana):
        if not nombre or not email or not password:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            self.usuario_service.registrar_usuario(nombre, email, password)
            messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente")
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el usuario: {str(e)}")

    def abrir_tienda(self):
        root = Tk()
        app = TiendaApp(root)
        root.mainloop()