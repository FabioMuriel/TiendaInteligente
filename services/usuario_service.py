# services/usuario_service.py
from models.usuario import Usuario
from database.database import Database

class UsuarioService:
    def __init__(self):
        self.db = Database("tienda_inteligente.db")

    def registrar_usuario(self, nombre, email, password):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)", (nombre, email, password))
        conn.commit()
        conn.close()

    def autenticar_usuario(self, email, password):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND password = ?", (email, password))
        usuario = cursor.fetchone()
        conn.close()
        return Usuario(*usuario) if usuario else None