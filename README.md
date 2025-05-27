# 💰 Sana — Tu guía para unas finanzas saludables

**Sana** es una aplicación de escritorio desarrollada en Python con Tkinter y SQLite que permite registrar, visualizar y analizar ingresos y gastos personales. Este proyecto forma parte del curso _Desarrollo de Aplicaciones de Escritorio con Python y Tkinter_, y tiene como objetivo aplicar los conocimientos adquiridos en un caso práctico completo.

---

## 🧩 Funcionalidades

- ✅ Registro de ingresos y gastos
- ✅ Clasificación por categorías
- ✅ Visualización de transacciones con filtros
- ✅ Resumen de ingresos, gastos y saldo actual
- ✅ Gestión de categorías personalizadas
- 🔄 Exportación de datos (CSV) *(opcional)*
- 📊 Gráficos de análisis *(opcional en versiones futuras)*

---

## 🧰 Tecnologías utilizadas

- Python 3.x
- Tkinter (interfaz gráfica)
- SQLite (base de datos local)
- ttk / ttkbootstrap *(estilización opcional)*

---

## 🗂 Estructura del proyecto

sana/

├── main.py # Punto de entrada

├── ui/ # Interfaz gráfica

│ ├── ventana_principal.py

│ ├── ventana_transacciones.py

│ ├── ventana_categorias.py

│ └── estilos.py

├── controllers/ # Lógica de control

│ ├── transacciones_controller.py

│ └── categorias_controller.py

├── models/ # Estructura de datos

│ ├── transaccion.py

│ └── categoria.py

├── db/ # Acceso a base de datos

│ ├── conexion.py

│ └── inicializar_db.py

├── utils/ # Funciones auxiliares

│ └── helpers.py

└── data/

└── sana.db # Base de datos SQLite


---

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/sana.git
cd sana
2. Asegúrate de tener Python 3 instalado.

3. Ejecuta el archivo principal:

python main.py
```

📚 Requisitos del curso
Este proyecto forma parte del programa formativo, y se desarrolla de manera guiada en clase. Al completarlo, habrás puesto en práctica:

* Creación de interfaces con Tkinter

* Conexión y operaciones con SQLite

* Organización modular de código

* Principios de diseño funcional de una app

📌 Licencia
Este proyecto es de uso educativo y está licenciado bajo los términos de uso del curso. Puedes modificarlo libremente con fines de aprendizaje.

✨ Autor
Letitech
💻 Curso: Desarrollo de Aplicaciones de Escritorio
📧 Contacto: letitech.sl@gmail.com
