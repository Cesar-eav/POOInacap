# Requisitos:
# Crear una tabla llamada productos en una base de datos SQLite, con las siguientes

# columnas:
    # - id: Identificador único (autoincremental).
    # - nombre: Nombre del producto (texto, no nulo).
    # - categoria: Categoría del producto (texto, no nulo).
    # - precio: Precio del producto (número entero, no nulo).
    # - stock: Cantidad de stock disponible (número entero, no nulo).

import sqlite3

def crear_tabla():
    try:

        #Conexión BD
        conn = sqlite3.connect('productos.db')

        cursor = conn.cursor()

        cursor.execute('''

        CREATE TABLE IF NOT EXISTS productos(
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    precio INTEGER NOT NULL,
                    stock INTEGER NOT NULL    
                    )
        ''')

        conn.commit()
        print("Tabla productos creada exitosamente")
        
    except sqlite3.DatabaseError as e:
        print(f'Error al crear la tabla productos: {e}')
    
    finally:        
        conn.close()