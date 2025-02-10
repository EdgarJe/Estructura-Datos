    Arreglo Bidimensional:
        El arreglo ventas tiene 3 filas (uno por cada departamento: Ropa, Deportes, Juguetería) y 12 columnas (para los 12 meses del año).
        Los valores se inicializan en 0, indicando que no hay ventas registradas al inicio.

    Funciones:
        mostrar_menu: Muestra un menú para que el usuario elija una opción (insertar, buscar, borrar, mostrar o salir).
        insertar_venta: Permite al usuario ingresar el monto de una venta para un departamento y mes específicos.
        buscar_venta: Permite al usuario consultar el monto de la venta para un departamento y mes específicos.
        borrar_venta: Permite al usuario borrar una venta registrada (pone el monto en 0).
        mostrar_ventas: Muestra todas las ventas registradas en la tienda, mes por mes y departamento por departamento.

    Ciclo Principal:
        El programa ejecuta un ciclo while que sigue mostrando el menú hasta que el usuario elige salir (opción 5).

Cómo funciona el programa:

    El usuario interactúa con el menú para ingresar ventas, buscar ventas por departamento y mes, eliminar ventas, o ver todas las ventas registradas.
    La validación de datos asegura que las opciones de departamento y mes estén dentro de los rangos correctos.