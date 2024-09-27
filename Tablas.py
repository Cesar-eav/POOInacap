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
                    precio INTEGER NOT NULL,
                    stock INTEGER NOT NULL,
                    categoria_id INTEGER,
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)        
                    )
        ''')

        conn.commit()
        print("Tabla productos creada exitosamente")
        
    except sqlite3.DatabaseError as e:
        print(f'Error al crear la tabla productos: {e}')
    
    finally:        
        conn.close()


def crear_tabla_categorias():
    try:

        #Conexión BD
        conn = sqlite3.connect('productos.db')

        cursor = conn.cursor()

        cursor.execute('''

        CREATE TABLE IF NOT EXISTS categorias(
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL 
                    )
        ''')

        conn.commit()
        print("Tabla categorias creada exitosamente")
        
    except sqlite3.DatabaseError as e:
        print(f'Error al crear la tabla categorias: {e}')
    
    finally:        
        conn.close()

        

