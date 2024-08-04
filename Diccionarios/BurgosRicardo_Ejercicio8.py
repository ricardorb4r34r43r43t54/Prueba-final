while True:
 diccionario = {} #Se crea un diccionario vacio
 palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ") #El programa le pide al usuario que ingrese una lista de palabras con su traduccion
 for i in palabras.split(','): #Dividimos la entrada del usuario en palabras y traducciones individuales, usando ',' como delimitador
    clave, valor = i.split(':') #Dividimos cada par palabra:traducción en sus componentes separados
    diccionario[clave] = valor #Asignamos la palabra como clave y la traducción como valor en el diccionario
 frase = input('Introduce una frase en español: ') #Le pedimos al usuario que ingrese una frase en español
 for i in frase.split(): #Dividimos la frase en palabras individuales
    if i in diccionario: #Verifica si la palabra esta en el diccionario
        print(diccionario[i], end=' ')  #Si la palabra está en el diccionario, imprime su traduccion
    else: #Si no
        print(i, end=' ') #Imprime en pantalla la frase tal y como se ingreso

 continuar = input("¿Deseas continuar? (s/n): ")  #Pregunta al usuario si desea continuar
 
 if continuar.lower() != "s":  #Si la respuesta no es "s" (o "S")
     break #Termina el bucle