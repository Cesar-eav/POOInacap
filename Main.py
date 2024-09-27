from FuncionesBD import *
from ProductosBD import *
from Tablas import *

crear_tabla()

crear_tabla_categorias()
add_categoria("Frutas")
add_categoria("Verduras")
add_categoria("Bebestibles")

mostrar_menu()


# menu:
# opcion 1 : ingresar add_producto

# funcion _ingresar_productos() -> input para que el usuario interactue
# funcion validar_datos() -> valido los datos con mi logica de negocio
# funcion insertar_datos() -> funcion que insertaen la BD


# add_producto(nombre, categoria, precio, stock):
# get_productos()

# id_producto = input("Dame el ID del producto a modificar: ")

# update_prduct(id_producto)

# id_producto = input("Dame el ID del producto a Eliminar: ")

# delete_product(id_producto)

# add_producto("Billetera ", "Accesorios", 5000, 2)
# add_producto("Cerveza ", "Bebestibles", 5000, 2)
# add_producto("Agua Mineral", "Bebestibles", 5000, 2)

# categoria = input("Introduce la categoria a buscar: ")

# search_product(categoria)


# get_productos()

# producto_a_buscar = input("Ingresa nombre del producto")

# search_product(producto_a_buscar)