#Este programa  permite al usuario ingresar informacion sobre una persona y la almacena en un diccionario hasta que decida que ya no desea agregar más informacion
persona = {}  #El diccionario almacena informacion de la persona
continuar = True  #Esta variable controla la informacion que se siga agregando

while continuar: #Es un bucle infinito
    clave = input('¿Qué dato quieres introducir? ')  #Le pide al usuario (tipo de información)
    valor = input(clave + ': ')  #Le pide al usuario un valor a la clave
    
    if valor:  #Verificar si se ingreso un valor valido (no vacío)
        persona[clave] = valor  #Almacena la clave y valor en el diccionario 'persona'
        print(f'Información añadida: {clave}: {valor}')  #Muestra en pantalla el mensaje de confirmacion
    else: #Si no
        print('¡No se ha ingresado ningún valor!')  #Muestra en pantalla el mensaje de error si no se ingreso valor

    respuesta = input('¿Quieres añadir más información (Si/No)? ').lower()  #Le pregunta al usuario si quiere continuar
    if respuesta != 'si':  #Si la respuesta no es 'si', salir del bucle
        continuar = False #Salir del bucle

print('Proceso de ingreso de información finalizado.')  #Muestra en pantalla el mensaje de finalizacion del proceso
