#menu
from base_datos import crear_tabla
from funciones import (
    registrar_producto,
    visualizar_productos,
    actualizar_producto,
    eliminar_producto,
    buscar_por_id,
    buscar_por_nombre_categoria,
    reporte_stock_bajo
)

def mostrar_menu():
    """
    Muestra el menú principal e interactúa con el usuario.
    """
    crear_tabla()

    while True:
        print("\n=== MENÚ DE INVENTARIO ===")
        print("1. Registrar nuevo producto")
        print("2. Ver productos registrados")
        print("3. Actualizar producto por ID")
        print("4. Eliminar producto por ID")
        print("5. Buscar producto por ID")
        print("6. Buscar por nombre o categoría")
        print("7. Reporte de stock bajo")
        print("8. Salir")

        opcion = input("Seleccioná una opción: ")
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            visualizar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_por_id()
        elif opcion == '6':
            buscar_por_nombre_categoria()
        elif opcion == '7':
            reporte_stock_bajo()
        elif opcion == '8':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")
