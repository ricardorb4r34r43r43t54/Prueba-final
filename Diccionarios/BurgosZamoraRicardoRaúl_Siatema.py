#Este programa es un sistema de inventario basico que le permite al usuario agregar producto, vender, mostar inventario y salir
inventario = [] #Se crea lista vacia llamada inventario, para almacenar el stock que se agregue

while True: #Inicio del bucle
    # Mostrar el menú al usuario
    print("Bienvenido:")
    print("1. Agregar producto")  #Opcion para agregar producto
    print("2. Vender producto")  #Opcion para vender producto
    print("3. Mostrar inventario")  #Opcion que muestra el stock en existencia
    print("4. Salir")  #Salir del programa

    opcion = input("Seleccione una opción: ") #Le pide al usuario que seleccione una opcion

    if opcion == '1': # Opcion 1: Agregar producto al inventario
        nombre_producto = input("Ingrese el nombre del producto: ")  #Le pide al usuario el nombre del producto
        cantidad_producto = int(input(f"Ingrese la cantidad de unidades de {nombre_producto}: "))  #Le pide al usuario que ingrese la cantidad del producto
        precio_producto = float(input(f"Ingrese el precio unitario de {nombre_producto}: Q"))  #Le pide al usuario el precio del producto
        inventario.append([nombre_producto, cantidad_producto, precio_producto]) #Agrega el producto al inventario como una lista 
        print("Producto agregado al inventario.")  #Indica que el producto fue agregado
   
    elif opcion == '2':  # Opcion 2: Vender producto del inventario
        producto_vender = input("Ingrese el nombre del producto a vender: ")  #Le pide al usuario que ingrese el nombre del producto a vender
        encontrado = False #Si no se encuentra el producto
       
        for producto in inventario:  #Busca el producto en el inventario
            if producto[0] == producto_vender: #Verifica si el nombre del producto es valida
                print(f"El precio unitario de {producto_vender} es: Q{producto[2]}")  #Muestra en pantalla el precio del producto
                cantidad_vender = int(input("Ingrese la cantidad de unidades a vender: "))  #Le pide la cantidad a vender
                
                if cantidad_vender <= producto[1]: #Verifica si hay suficientes unidades
                    pago = float(input("Ingrese la cantidad con la que pagara: Q"))  #Solicita el pago del cliente
                    total_a_pagar = cantidad_vender * producto[2]  #Calcula el total a pagar
                    if pago >= total_a_pagar:  #Verifica si el pago es suficiente
                        cambio = pago - total_a_pagar  #Calcula el cambio
                        producto[1] -= cantidad_vender  #Actualiza la cantidad en inventario despues de la venta
                        print(f"Venta exitosa: {cantidad_vender} unidades de {producto_vender} vendidas.") #Muestra en pantalla que la venta fue exitosa, junto con la cantidad a vender y las unidades que venderan
                        print(f"Su cambio es: Q{cambio}")  #Muestra en pantalla el cambio al cliente
                    else: #Si no
                        print("El pago no es suficiente.")  #Informa al cliente si el pago no es suficiente
                else: #Si no 
                    print("No hay suficientes unidades")  #Informa al cliente si no hay suficientes unidades
                encontrado = True #Si se encuentra el producto
                break #Para salir del bucle
       
        if not encontrado:  #Si el producto no está en el inventario
            print("El producto no esta en inventario.")  #Muestra en pantalla que el producto no esta en el inventario

    elif opcion == '3':  #Opcion 3: Mostrar el inventario actualizado
        print("\nInventario actualizado:")  #Muestra en pantalla que el inventario esta actualizado
        for producto in inventario:
            print(f"{producto[0]}: {producto[1]} unidades - Precio: Q{producto[2]}")  # Mostra en pantalla cada producto que esta inventario

    elif opcion == '4':  #Opcion 4: Salir del programa
        print("Gracias por utilizar el programa. ¡Pronto cobraremos por su uso!")  # Despedirse del usuario
        break  #Salir del bucle 

    else:  #Si el usuario ingresa una opcion no valida
        print("Opcion no valida. Por favor, seleccione una opción válida.")  #Muestra en pantalla que la opcion no es valida
