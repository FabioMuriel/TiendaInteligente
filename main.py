from tkinter import Tk
from ui.login import LoginApp
from database.database import Database

if __name__ == "__main__":
    # Crear la base de datos y tablas si no existen
    db = Database("tienda_inteligente.db")
    db.create_tables()

    # Iniciar la aplicación con la ventana de login
    root = Tk()
    app = LoginApp(root)
    root.mainloop()