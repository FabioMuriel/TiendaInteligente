# main.py
from tkinter import Tk
from ui.gui import TiendaApp
from database.database import Database

if __name__ == "__main__":
    # Crear la base de datos y tablas si no existen
    db = Database("tienda_inteligente.db")
    db.create_tables()

    # Iniciar la aplicación
    root = Tk()
    app = TiendaApp(root)
    root.mainloop()