import serial

# Inicialización del puerto serial
lectura = serial.Serial('COM3', 9600)

# Funciones para controlar los LEDs
def encender_led1():
    """
    Enciende el primer LED enviando el byte '1' por el puerto serial.
    """
    lectura.write(b'1')

def apagar_led1():
    """
    Apaga el primer LED enviando el byte '0' por el puerto serial.
    """
    lectura.write(b'0')

def encender_led2():
    """
    Enciende el segundo LED enviando el byte '2' por el puerto serial.
    """
    lectura.write(b'2')

def apagar_led2():
    """
    Apaga el segundo LED enviando el byte '3' por el puerto serial.
    """
    lectura.write(b'3')

def encender_led3():
    """
    Enciende el tercer LED enviando el byte '4' por el puerto serial.
    """
    lectura.write(b'4')

def apagar_led3():
    """
    Apaga el tercer LED enviando el byte '5' por el puerto serial.
    """
    lectura.write(b'5')

def encender_led4():
    """
    Enciende el cuarto LED enviando el byte '6' por el puerto serial.
    """
    lectura.write(b'6')

def apagar_led4():
    """
    Apaga el cuarto LED enviando el byte '7' por el puerto serial.
    """
    lectura.write(b'7')

# Inicio del ciclo While
while True:
    comando = input("Escribe 'encender1', 'apagar1', 'encender2', 'apagar2', 'encender3', 'apagar3', 'encender4' o 'apagar4' para controlar los LEDs: ").strip().lower()
    
    if comando == 'encender1':
        encender_led1()
        print("LED 1 encendido")
    elif comando == 'apagar1':
        apagar_led1()
        print("LED 1 apagado")
    elif comando == 'encender2':
        encender_led2()
        print("LED 2 encendido")
    elif comando == 'apagar2':
        apagar_led2()
        print("LED 2 apagado")
    elif comando == 'encender3':
        encender_led3()
        print("LED 3 encendido")
    elif comando == 'apagar3':
        apagar_led3()
        print("LED 3 apagado")
    elif comando == 'encender4':
        encender_led4()
        print("LED 4 encendido")
    elif comando == 'apagar4':
        apagar_led4()
        print("LED 4 apagado")
    else:
        print("Comando no reconocido. Por favor escribe 'encender1', 'apagar1', 'encender2', 'apagar2', 'encender3', 'apagar3', 'encender4' o 'apagar4'.")
