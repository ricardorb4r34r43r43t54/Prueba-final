#Este programa le permite al usuario administrar clientes, permitiendo al usuario visualizar su informacion
clientes = {}  #Este diccionario almacena los clientes
opcion = ''  #Variable para almacenar la opcion del menu seleccionada
while opcion != '6':  #Bucle principal, continuara hasta que se seleccione la opción 6 (Terminar)
    if opcion == '1':  #Si la opcion seleccionada es 1 (Añadir cliente)
        nif = input('Introduce NIF del cliente: ') #Le pide al usuario su NIF
        nombre = input('Introduce el nombre del cliente: ') #Le pide al usuario su nombre
        direccion = input('Introduce la dirección del cliente: ') #Le pide al usuario su direccion
        telefono = input('Introduce el teléfono del cliente: ') #Le pide al usuario su telefono
        email = input('Introduce el correo electrónico del cliente: ') #Le pide al usuario su email
        vip = input('¿Es un cliente frecuente (S/N)? ') #Le pregunta al usuario si es precuente
        
        cliente = {'nombre': nombre, 'dirección': direccion, 'teléfono': telefono, 'email': email, 'frecuente': vip == 'S'} #Se crea un diccionario con la información del cliente
        clientes[nif] = cliente #Se agrega al diccionario de clientes
    if opcion == '2':  #Si la opciOn seleccionada es 2 (Eliminar cliente)
        nif = input('Introduce NIF del cliente: ') #Le solicita el NIF del cliente al usuario
        if nif in clientes: #Verifica si el cliente con el NIF proporcionado existe en el diccionario de clientes
            del clientes[nif] # Si existe, se elimina del diccionario de clientes
        else: #Si no
            print('No existe el cliente con el nif', nif) #Muestra un mensaje indicando que el cliente no existe
    if opcion == '3':  #Si la opciOn seleccionada es 3 (Mostrar cliente)
        nif = input('Introduce NIF del cliente: ') #Le solicita el NIF del cliente al usuario
        if nif in clientes: #Verifica si el cliente con el NIF proporcionado existe en el diccionario de clientes
            print('NIF:', nif) # Si existe, se muestra la información del cliente
            for clave, valor in clientes[nif].items(): #Esta iterando sobre todos los pares clave-valor dentro del diccionario
                print(clave.title() + ':', valor) #Imprime en pantalla los valores de la variable clave y valor
        else: # Si no
            print('No existe el cliente con el nif', nif) #Muestra en pantalla un mensaje indicando que el cliente no existe
    if opcion == '4':  #Si la opcion seleccionada es 4 (Listar clientes)
        print('Lista de clientes') #Muestra en pantalla una lista de todos los clientes y sus NIF
        for clave, valor in clientes.items(): #Esta iterando sobre todos los pares clientes dentro del diccionario
            print(clave, valor['nombre']) #Imprime en pantalla los valores de la variable clave, lo mismo con la variable nombre, dentro del diccionario valor
    if opcion == '5':  #Si la opcion seleccionada es 5 (Listar clientes preferentes)
        print('Lista de clientes frecuentes') #Muestra una lista de clientes preferentes y sus NIF
        for clave, valor in clientes.items(): #Esta iterando sobre todas las claves y valores dentro del diccionario clientes
            if valor['frecuente']: #Si el usuario es frecuente
                print(clave, valor['nombre']) #Imprime en pantalla su clave, valor del nombre
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes frecuentes\n(6) Terminar\nElige una opción:') #Le vuelve a solicitar al usuario que elija una opción del menu
    
    continuar = input("¿Deseas continuar? (s/n): ")  # Pregunta al usuario si desea continuar
    if continuar.lower() != "s":  # Si la respuesta no es "s" (o "S")
        break  # Termina el bucle
