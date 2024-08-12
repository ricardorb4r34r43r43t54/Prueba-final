# Importa el módulo unicodedata, que proporciona funciones para acceder a la base de datos de caracteres Unicode.
# Esto incluye la obtención de nombres de caracteres, normalización de cadenas, y manipulación de acentos.
import unicodedata

def normalizar_texto(texto):
    """ Normaliza el texto eliminando acentos y convirtiendo a minusculas """
    texto = texto.lower()  # Convertir a minúsculas
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto

def mostrar_menu():
    """ Muestra el menu principal """
    print("\n" + "="*40)
    print(" " + "Diccionario RB".center(38))
    print("="*40)
    print(" " + "Bienvenido/a".center(38))
    print("="*40)
    print("1. Buscar término")
    print("2. Buscar por palabra clave")
    print("3. Buscar por definición exacta")
    print("4. Salir")
    print("="*40)

def buscar_palabra(diccionario):
    """ Busca un término en el diccionario, sin importar tildes, mayúsculas o minúsculas """
    termino = input("Ingrese un término para buscar su definición: ").strip()
    termino_normalizado = normalizar_texto(termino)
    
    if termino_normalizado in diccionario:
        termino_original, definicion = diccionario[termino_normalizado]
        print(f"\n{termino_original}: {definicion}\n")
    else:
        print("El término no está en el diccionario.\n")

def buscar_palabra_clave(diccionario):
    """ Busca términos por definición """
    palabra_clave = input("Ingrese una palabra clave para buscar en las definiciones: ").strip()
    palabra_clave_normalizada = normalizar_texto(palabra_clave)
    encontrado = False
    
    print("\nResultados de búsqueda por palabra clave:")
    print("="*40)
    for termino_normalizado, (termino_original, definicion) in diccionario.items():
        if palabra_clave_normalizada in normalizar_texto(definicion):
            print(f"{termino_original}: {definicion}")
            encontrado = True
            
    if not encontrado:
        print("No se encontró ninguna definición que contenga la palabra clave.")
    print("="*40)

def buscar_definicion_completa(diccionario):
    """ Busca términos por definición completa """
    definicion = input("Ingrese la definición exacta que desea buscar: ").strip()
    definicion_normalizada = normalizar_texto(definicion)
    encontrado = False
    
    print("\nResultados de búsqueda por definición completa:")
    print("="*40)
    for termino_normalizado, (termino_original, definicion_diccionario) in diccionario.items():
        if definicion_normalizada == normalizar_texto(definicion_diccionario):
            print(f"{termino_original}: {definicion_diccionario}")
            encontrado = True
    
    if not encontrado:
        print("No se encontró ninguna definición que coincida exactamente.")
    print("="*40)

# Se crea la lista diccionario, la cual almacena palabras con sus respectivos significados
diccionario_informativo = { 
    "Algoritmo": "Un algoritmo es una secuencia finita de pasos",
    "Arrastrar": "Ocurre cuando un usuario apunta el mouse hacia un ícono o carpeta",
    "Barra de desplazamiento": "Permite al usuario controlar qué parte del documento está visible en la ventana",
    "Base de datos": "Un gran conjunto estructurado de datos",
    "Boot": "El proceso de cargar o inicializar un sistema operativo en una computadora",
    "Byte": "Pequeña unidad de almacenamiento de datos",
    "Cache": "Una memoria local pequeña y rápida",
    "Carpeta": "Organiza una colección de archivos de computadora",
    "Clic": "Ocurre cuando un usuario presiona un botón",
    "Descargar": "Transferencia de datos de otra computadora a su computadora",
    "Microprocesador": "Unidad central de procesamiento de una computadora",
    "Supercomputadoras": "Computadoras extremadamente rápidas y potentes",
    "Sistema": "Conjunto de componentes interrelacionados",
    "Red": "Conexión de computadoras para compartir recursos",
    "Almacenamiento": "Lugar donde se guardan datos",
    "Nube": "Servicios en línea accesibles por internet",
    "Hub": "Dispositivo para conectar varios dispositivos en una red",
    "MAN": "Red de área metropolitana",
    "PAN": "Red de área personal",
    "LAN": "Red de área local",
    "WAN": "Red de área amplia",
    "GAN": "Red de área global",
    "VPN": "Red privada virtual",
    "Desarrollo": "Proceso de creación de software",
    "IA": "Inteligencia artificial",
    "Software libre": "Software que se puede usar, modificar y distribuir libremente",
    "Código abierto": "Código fuente accesible públicamente",
    "Software de propietario": "Software con restricciones de uso y modificación",
    "Computadora": "Dispositivo electrónico para procesar datos",
    "Teclado": "Dispositivo para introducir datos mediante teclas",
    "Impresora": "Dispositivo que produce una copia física de documentos",
    "Tipología": "Clasificación de tipos o categorías",
    "Tipología Bus": "Arquitectura de red en bus",
    "Ethernet": "Tecnología de red local basada en cables",
    "Token ring": "Red en la que los datos viajan en un anillo",
    "Arcnet": "Tecnología de red en estrella",
    "Tester": "Dispositivo para medir circuitos electrónicos",
    "Ponchadora": "Herramienta para hacer agujeros en tarjetas perforadas",
    "Conectores": "Dispositivos para unir cables y equipos",
    "Arduino": "Plataforma de hardware libre para prototipos electrónicos",
    "Arduino Mega": "Versión avanzada de la placa Arduino",
    "Jumpers": "Pequeños conectores para cambiar configuraciones de hardware",
    "Módulo RFID": "Dispositivo para leer y escribir etiquetas RFID",
    "Sensor de temperatura y Humedad": "Dispositivo para medir temperatura y humedad",
    "Led": "Diodo emisor de luz",
    "Resistencia": "Componente que limita el flujo de corriente",
    "Potenciómetro": "Resistencia variable ajustable",
    "Photoball": "Dispositivo que detecta luz",
    "Pantalla LCD": "Pantalla de cristal líquido",
    "Motor Stepper": "Motor que se mueve en pasos precisos",
    "Motor DC": "Motor de corriente continua",
    "Módulo relé": "Dispositivo para controlar circuitos de alta potencia",
    "Servomotor": "Motor con control preciso de posición",
    "Joystick": "Dispositivo de entrada para controlar gráficos o movimiento",
    "Gamer": "Persona que juega videojuegos",
    "Fibonacci": "Secuencia matemática en la que cada número es la suma de los dos anteriores",
    "Normativa": "Conjunto de reglas o estándares",
    "Word": "Procesador de texto de Microsoft",
    "Excel": "Hoja de cálculo de Microsoft",
    "Power Point": "Programa de presentaciones de Microsoft",
    "Office 365": "Suite de productividad basada en la nube de Microsoft",
    "Microsoft": "Empresa de tecnología y software",
    "Bethesda": "Desarrollador de videojuegos",
    "Nintendo": "Empresa de videojuegos",
    "Halo": "Franquicia de videojuegos de disparos en primera persona",
    "Mark V": "Versión de un casco de poder en la serie Halo",
    "Lógica": "Estudio de principios del razonamiento",
    "Operadores relacionales": "Operadores para comparar valores",
    "Función": "Bloque de código que realiza una tarea específica",
    "HP": "Marca de computadoras y tecnología",
    "Ciclo For": "Estructura de control para repetir una acción un número definido de veces",
    "Ciclo While": "Estructura de control que repite una acción mientras se cumpla una condición",
    "Diagrama de flujo": "Representación gráfica de un algoritmo",
    "Laptop": "Computadora portátil",
    "Windows": "Sistema operativo de Microsoft",
    "Máquina virtual": "Software que emula una computadora completa",
    "Mac OS": "Sistema operativo de Apple para computadoras Macintosh",
    "Linux": "Sistema operativo de código abierto",
    "Unix": "Sistema operativo multitarea",
    "Privacidad": "Protección de datos personales",
    "Derechos de autor": "Protección legal de obras originales",
    "Pseudocódigo": "Representación informal de un algoritmo",
    "Domótica": "Automatización de viviendas",
    "Print": "Instrucción para imprimir datos",
    "While True": "Bucle que se ejecuta indefinidamente",
    "If": "Estructura de control condicional",
    "Else": "Alternativa en una estructura condicional",
    "Librería": "Colección de funciones y procedimientos reutilizables",
    "Lista": "Estructura de datos que almacena una secuencia de elementos",
    "Tupla": "Estructura de datos inmutable que almacena una secuencia de elementos",
    "Variable": "Espacio de almacenamiento para datos",
    "Código": "Conjunto de instrucciones para un programa",
    "CPU": "Unidad central de procesamiento",
    "RAM": "Memoria de acceso aleatorio",
    "ROM": "Memoria de solo lectura",
    "Chip": "Circuito integrado en un solo componente",
    "Firmware": "Software integrado en hardware",
    "Sistema operativo": "Software que gestiona hardware y software",
    "Driver": "Software que permite la comunicación con hardware",
    "BIOS": "Sistema básico de entrada/salida",
    "Bus": "Sistema de comunicación entre componentes de una computadora",
    "Puerto": "Conector para dispositivos externos",
    "Resolución": "Número de píxeles en una pantalla",
    "GPU": "Unidad de procesamiento gráfico",
    "Redes sociales": "Plataformas para interactuar en línea",
    "Navegador": "Software para acceder a internet",
    "URL": "Localizador uniforme de recursos",
    "HTML": "Lenguaje de marcado para páginas web",
    "CSS": "Hojas de estilo en cascada para diseño web",
    "JavaScript": "Lenguaje de programación para interactividad web"
}

# Crear un diccionario normalizado, el normalizar_texto ayuda a poder escribir una palabra sin tildes o solo con mayusculas o minusculas, y aun asi el programa pueda buscar las palabras
diccionario_informativo_normalizado = {normalizar_texto(k): (k, v) for k, v in diccionario_informativo.items()}

def main():
    """
    Ejecuta un menú interactivo que permite al usuario buscar en un diccionario
    
    Ofrece opciones para buscar palabras, buscar por clave, obtener definiciones completas
    o salir del programa. Permite realizar múltiples búsquedas hasta que el usuario decida salir
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            buscar_palabra(diccionario_informativo_normalizado)
        
        elif opcion == '2':
            buscar_palabra_clave(diccionario_informativo_normalizado)
        
        elif opcion == '3':
            buscar_definicion_completa(diccionario_informativo_normalizado)
        
        elif opcion == '4':
            print("\nSigue usando el programa")
            break
        
        else:
            print("Opción inválida, seleccione una opción entre 1 y 4.\n")
        
        continuar = input("¿Desea realizar otra búsqueda? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nSigue usando el programa")
            break

if __name__ == "__main__":
    main()
