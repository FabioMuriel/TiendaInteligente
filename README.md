# **Mercado Inteligente - Proyecto de Gestión de Carrito de Compras**

Este proyecto es una aplicación de **Mercado Inteligente** desarrollada en Python, que permite a los usuarios gestionar un carrito de compras, calcular costos, aplicar descuentos y generar un recibo de compra. La aplicación utiliza **Tkinter** para la interfaz gráfica (GUI), **SQLite** para la base de datos y sigue los principios de la **Programación Orientada a Objetos (POO)**.

---

## **Tabla de Contenidos**
1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Funcionalidades](#funcionalidades)
5. [Capturas de Pantalla](#capturas-de-pantalla)
6. [Ejecución](#ejecución)
7. [Contribución](#contribución)
8. [Licencia](#licencia)

---

## **Requisitos**

- **Python 3.8 o superior**.
- **Tkinter**: Viene incluido con Python.
- **SQLite3**: Viene incluido con Python.

---

## **Instalación**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/mercado-inteligente.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd mercado-inteligente
   ```
3. (Opcional) Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Estructura del Proyecto**

```
tienda_inteligente/
│
├── database/
│   ├── __init__.py
│   ├── database.py
│
├── models/
│   ├── __init__.py
│   ├── producto.py
│   ├── carrito.py
│   ├── usuario.py
│
├── services/
│   ├── __init__.py
│   ├── carrito_service.py
│   ├── producto_service.py
│   ├── usuario_service.py
│
├── ui/
│   ├── __init__.py
│   ├── gui.py
│   ├── login.py
│
├── utils/
│   ├── __init__.py
│   ├── receipt.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## **Funcionalidades**

1. **Agregar productos al carrito**:
   - Los usuarios pueden agregar productos ingresando el nombre, precio y cantidad.
   - Los productos se almacenan en una base de datos SQLite.

2. **Calcular totales y descuentos**:
   - El sistema calcula automáticamente el total de la compra.
   - Aplica un descuento del 10% si se compran 3 o más productos.

3. **Generar recibo**:
   - Se genera un recibo detallado con la lista de productos, subtotales, descuentos y total a pagar.
   - El recibo se muestra en una ventana emergente con un diseño moderno y profesional.

4. **Interfaz gráfica moderna**:
   - La interfaz gráfica utiliza Tkinter con estilos modernos, colores atractivos y un diseño limpio.

---

## **Capturas de Pantalla**

### **Interfaz Principal**
![Interfaz Principal](screenshots/main_interface.png)

### **Recibo de Compra**
![Recibo de Compra](screenshots/receipt.png)

---

## **Ejecución**

1. Asegúrate de tener Python instalado.
2. Navega al directorio del proyecto:
   ```bash
   cd mercado-inteligente
   ```
3. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

---

## **Contribución**

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Añade nueva funcionalidad"
   ```
4. Sube tus cambios:
   ```bash
   git push origin nueva-funcionalidad
   ```
5. Abre un Pull Request en GitHub.

---

## **Licencia**

Este proyecto está bajo la licencia **MIT**. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---
