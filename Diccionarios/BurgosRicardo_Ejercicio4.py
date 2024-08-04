while True: #El bucle es infinito
 meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'} #Es el diccionario de los meses del año
 fecha = input('Introduce una fecha en formato dd/mm/aaaa: ') #Le pide al usuario que ingrese la fecha en formato dd/mm/aaaa
 fecha = fecha.split('/') #Divide la entrada en dia, mes y año
 print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])   #Imprime en pantalla la fecha en formato día de mes de año
