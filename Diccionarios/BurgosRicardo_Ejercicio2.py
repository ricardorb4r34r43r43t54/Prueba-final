#Este programa es un diccionario el cual usa variables para almacenar datos que se le piden al usuario y lo muestra en pantalla
while True: #Inicio del bucle
 nombre = input('¿Cómo te llamas? ') #La variable de nombre almacena el nombre que escribe el usuario
 edad = input('¿Cuántos años tienes? ') #La variable edad almacena la edad que escribe el usuario
 direccion = input('¿Cuál es tu dirección? ') #La variable direccion almacena la direccion que escribe el usuario
 telefono = input('¿Cuál es tu número de teléfono? ') #La variable de nombre almacena el nombre que escribe el usuario
 persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono} #El diccionario almacena a todas las variables anteriores
 print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono']) #Muestra en pantalla los elementos del diccionario

 continuar = input("¿Deseas continuar? (s/n): ")  #Pregunta al usuario si desea continuar
 
 if continuar.lower() != "s":  #Si la respuesta no es "s" (o "S")
     break #Termina el bucle