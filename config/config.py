from os import getenv
from pathlib import Path
import sqlite3

class DataBase:
    """Clase de configuración de la base de datos"""
    def __init__(self, db_name="db.db", data_dir="data"):
        """
        Inicializa el gestor de SQLite
        
        Args:
            db_name (str): Nombre del archivo de base de datos
            data_dir (str): Directorio donde se almacenará la base de datos
        """
        self.data_dir = Path(data_dir)
        self.db_path = self.data_dir / db_name

        # Crear directorio si no existe
        self.create_directory()
        self.create_tables()

    def create_directory(self):
        """Crea el directorio de datos si no existe"""
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def connect(self):
        """Establece conexión con la base de datos"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            return self.connection
        except sqlite3.Error as e:
            return None
        
    def disconnect(self):
        """Cierra la conexión con la base de datos"""
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        """
        Ejecuta una consulta SQL
        
        Args:
            query (str): Consulta SQL a ejecutar
            params (tuple): Parámetros para la consulta (opcional)
        """      
        try:
            cursor = self.connect().cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            self.connection.commit()
            return cursor
        except sqlite3.Error as e:
            return None
        
    def create_tables(self):
        """Crea tablas basadas en los esquemas proporcionados"""
        
        table_schemas = {
            "users": """(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )""",
            "categories": """(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user_id INTEGER,
                
                FOREIGN KEY (user_id) REFERENCES users(id)
            )""",
            "transactions": """(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL CHECK(type IN ('Ingreso', 'Gasto')),
                amount REAL NOT NULL,
                category_id INTEGER,
                user_id INTEGER,
                description TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (category_id) REFERENCES categories(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )""",
        }

        for table_name, schema in table_schemas.items():
            self.execute_query(f"CREATE TABLE IF NOT EXISTS {table_name} {schema}")