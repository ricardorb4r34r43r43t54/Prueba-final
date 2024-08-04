
inventario = []
 
while True:
    accion = input("¿Qué acción desea realizar? (agregar/vender/mostrar/salir): ")
 
    if accion == "agregar":
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad_producto = int(input(f"Ingrese la cantidad de unidades de {nombre_producto}: "))
        precio_producto = float(input(f"Ingrese el precio unitario de {nombre_producto}: Q"))
        inventario.append([nombre_producto, cantidad_producto, precio_producto])
        print("Producto agregado al inventario.")
 
    elif accion == "vender":
        producto_vender = input("Ingrese el nombre del producto a vender: ")
        encontrado = False
 
        for producto in inventario:
            if producto[0] == producto_vender:
                print(f"El precio unitario de {producto_vender} es: Q{producto[2]}")
                cantidad_vender = int(input("Ingrese la cantidad de unidades a vender: "))
 
                if cantidad_vender <= producto[1]:
                    pago = float(input("Ingrese la cantidad con la que pagará: Q"))
                    total_a_pagar = cantidad_vender * producto[2]
                    if pago >= total_a_pagar:
                        cambio = pago - total_a_pagar
                        producto[1] -= cantidad_vender
                        print(f"Venta exitosa: {cantidad_vender} unidades de {producto_vender} vendidas.")
                        print(f"Su cambio es: Q{cambio}")
                    else:
                        print("El pago no es suficiente.")
                else:
                    print("No hay suficientes unidades")
                encontrado = True
                break
 
        if not encontrado:
            print("El producto no está en inventario.")
 
    elif accion == "mostrar":
        print("\nInventario actualizado:")
        for producto in inventario:
            print(f"{producto[0]}: {producto[1]} unidades - Precio: Q{producto[2]}")
 
    elif accion == "salir":
        print("Gracias por utilizar el programa. ¡Pronto cobraremos por su uso!")
        break
 
    else:
        print("Acción no válida. Por favor, seleccione una acción válida.")