# Agregar un nuevo producto: 

import sqlite3

# Los usuarios deberán poder añadir un producto con su nombre, categoría, precio y stock.
def add_producto():
    while True:  
        conn = None
        try:

            nombre = input("Nombre Producto: ")
            get_categorias()
            categoria_id = int(input("Elegir Categoria: "))

            #PRECIO DEBE SER POSITIVO
            precio = int(input("Precio: "))

            if precio <= 0:
                print("El precio debe ser positivo")
                continue 
                    
            #STOCK DEBE SER POSITIVO
            stock = int(input("Stock: "))
            if stock <= 0:
                print("El Stock debe ser positivo")
                continue

        except ValueError:
            print("ValueError: Debes ingresar un valor numérico para el precio y el stock.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            
        # UNA VEZ VALIDADOS LOS DATOS SE INGRESAN A LA BD
        try:
            conn= sqlite3.connect('productos.db')
            cursor = conn.cursor()
            cursor.execute('''

            INSERT INTO productos (nombre, categoria_id, precio, stock) VALUES (?,?,?,?)
            ''', (nombre, categoria_id, precio, stock))

            conn.commit()
            print("Producto agregado exitosamente")

        except sqlite3.DatabaseError as e:
            print(f'Error al agregar producto: {e}')
        finally:
            if conn is not None:
                conn.close()
      
      
        while True:
            try:
                decision = int(input("Vuelve al menú(1) o Agrega Producto(2): "))

                if decision == 1:
                    mostrar_menu()
                elif decision == 2:
                    break
                else:
                    print("Opción no válida, ingresa 1 o 2.")
            except ValueError:
                print("ValueError: Debes ingresar un número válido (1 o 2).")


#FUNCION CREA CATEGORIAS INGRESADAS EN MAIN,
#EL USUARIO NO PUEDE CREAR NUEVAS CATEGORIAS.
def add_categoria(nombre):
    try:
        conn= sqlite3.connect('productos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id FROM categorias WHERE nombre = ?', (nombre,))
        categoria_existente = cursor.fetchone()
        
        #EVITAR CREAR CATEGORIAS EXISTENTES AL INICIAR PROGRAMA
        if categoria_existente:
            print(f"La categoría '{nombre}' ya existe.")

        else:
            cursor.execute('''
                    
            INSERT INTO categorias (nombre) VALUES (?)
                    ''', (nombre,))

            conn.commit()
            print(f"Categoria {nombre}  agregado exitosamente")
            
    except sqlite3.DatabaseError as e:
        print(f'Error al crear la tabla categorias: {e}')
    
    finally:        
        conn.close()

    
def get_categorias():
    conn = None
    try:
        conn = sqlite3.connect('productos.db')
        
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categorias')

        categorias = cursor.fetchall()

        if categorias:
            print("=== Elegir Categoria del Producto ===")
            for categoria in categorias:
                print(f" {categoria[0]} - {categoria[1]}")
        else:
            print("No hay categorias")
    except sqlite3.DatabaseError as e:
        print(f'Error en DataBase: {e}')

    finally:
        conn.close()


# - Listar todos los productos: Consultar y mostrar todos los productos almacenados.
def listar_productos():
    conn = None

    try:
        conn = sqlite3.connect('productos.db')
        
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT productos.id, productos.nombre, productos.precio, productos.stock, categorias.nombre  
                       FROM PRODUCTOS
                       INNER JOIN categorias ON productos.categoria_id =categorias.id
                       ''')
        productos = cursor.fetchall()

        if productos:
            for producto in productos:
                print(producto)
        else:
            print("No hay productos")
    except sqlite3.DatabaseError as e:
        print(f'Error al agregar producto: {e}')

    finally:
        conn.close()


# - Buscar productos por categoría: Consultar productos según la categoría especificada por el usuario.

def search_product():
    
    while True:  
        conn = None
        
        try:       
            get_categorias()  
            categoria_id = int(input("Introduce el ID de la categoria: "))
            
            if categoria_id <=0:
                print("Numero inválido")
                continue
                
        except ValueError:
            print("Debes ingresar un número")
            continue
             
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
                    

        try:
            conn = sqlite3.connect('productos.db')
            cursor = conn.cursor()
                        
                        
            cursor.execute('''
                SELECT productos.id, productos.nombre, productos.precio, productos.stock 
                FROM productos
                WHERE productos.categoria_id = ?

            ''', (categoria_id,)) 

            productos = cursor.fetchall()

            if productos:
    
                for producto in productos:
                    print( f"Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]},  ")
        
            else:
                print(f"No existe la cateogria")
        
        except sqlite3.DatabaseError as e:
            print(f"Error al buscar producto: {e}")

        finally:
            if conn is not None:
                conn.close()
            
        while True:
            try:
                decision = int(input("Vuelve al menú(1) o Buscar nuevamente(2): "))

                if decision == 1:
                    mostrar_menu()
                elif decision == 2:
                    break
                else:
                    print("Opción no válida, ingresa 1 o 2.")
            except ValueError:
                print("ValueError: Debes ingresar un número válido (1 o 2).")



# - Actualizar el precio y el stock de un producto existente.

def update_prduct():
    
    while True:
        conn = None
        
        try:
            listar_productos()
            id_producto = int(input("Dame el ID del producto a modificar: "))
            
            if id_producto <=0:
                print("ID Inválido")
                continue
            
        except ValueError:
            print("Debes ingresar un numero valido")
            continue
        
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

            
        try:
            print("*****************CONECTANDO***************")
            conn = sqlite3.connect('productos.db')
            cursor = conn.cursor()
            cursor.execute('''
                        
                        SELECT * FROM productos
                                WHERE id = ?
                        
                        ''', (id_producto,))
            
            producto = cursor.fetchall()
            
            
            if producto == []:

                print("ID NO EXISTE.")
                continue
            
            print("***************** FIN CONECTANDO***************")

        except sqlite3.DatabaseError as e:
            print(f'Error al obtener producto: {e}')
            
     



        print(f"{producto}")
      

        if producto:
            for p in producto:
                print("----TU PRODUCTO----")
                print(f"Id: {p[0]}, Nombre: {p[1]}, Categoría: {p[2]}, Precio: {p[3]}, Stock: {p[4]}")

            nuevo_precio = int(input("Ingresar nuevo precio: "))
            nuevo_stock = int(input("Ingresar Stock: "))

            cursor.execute('''
                UPDATE productos
                    SET precio = ?, stock = ?
                    WHERE id = ?
                        
                    

            ''',(nuevo_precio,nuevo_stock,id_producto ) )

            conn.commit()

            print(f"Producto con ID {id_producto} ha sido actualizado con éxito.")
            print(f"Nuevo precio: {nuevo_precio}, Nuevo stock: {nuevo_stock}")
        
        
        else:
            print("NO EXISTE EL PRODUCO / ID")

            conn.close()




    


# - Eliminar un producto según su ID.
# Manejar errores de conexión, errores en consultas mal formadas, 
# o en la operación de la base de datos 
# (como intentar actualizar o eliminar un producto que no existe).

def delete_product():
    listar_productos()
    id_producto = int(input("Dame el id del producto: "))
    try:
        conn = sqlite3.connect('productos.db')
        cursor = conn.cursor()

        cursor.execute('''

            SELECT * FROM productos
                WHERE id = ? 

            ''',(id_producto,))
        
        producto = cursor.fetchone()

        if producto:
            cursor.execute('''

            DELETE FROM productos
                WHERE id = ?

            ''',(id_producto,))
            print(f"{producto[0]} eliminado")
            conn.commit()

        else:
            print("No existe el ID del producto que buscas")
    
    except sqlite3.DatabaseError as e:
        print(f'DatabaseError: {e}')

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
      
    
    conn.close()


def mostrar_menu():
    """Mostrar el menú principal"""
    while True:
        print("\n=== Menú de Productos ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto por cateogia")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            add_producto()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            search_product()
        elif opcion == '4':
            update_prduct()
        elif opcion == '5':
            delete_product()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")