def suma(a, b):
    """
    Realiza la operación de suma entre dos números.

    Args:
    a (float or int): Primer número.
    b (float or int): Segundo número.
    
    Returns:
    float or int: Resultado de la suma de a y b.
    """
    return a + b

def resta(a, b):
    """
    Realiza la operación de resta entre dos números.

    Args:
    a (float or int): Primer número.
    b (float or int): Segundo número.
    
    Returns:
    float or int: Resultado de la resta de a y b.
    """
    return a - b

def multiplicacion(a, b):
    """
    Realiza la operación de multiplicación entre dos números.

    Args:
    a (float or int): Primer número.
    b (float or int): Segundo número.
    
    Returns:
    float or int: Resultado de la multiplicación de a y b.
    """
    return a * b

def division(a, b):
    """
    Realiza la operación de división entre dos números.

    Args:
    a (float or int): Numerador.
    b (float or int): Denominador distinto de cero.
    
    Returns:
    float: Resultado de la división de a entre b.
    
    Raises:
    ValueError: Si el denominador b es cero.
    """
    if b == 0:
        raise ValueError("El denominador no puede ser cero.")
    return a / b

if __name__ == "__main__":
    #Le solicita al usuario la entrada de datos al usuario
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        #Muestra en pantalla los resultados de las operaciones
        print(f"\nOperaciones con {num1} y {num2}:")
        print("Suma:", suma(num1, num2))
        print("Resta:", resta(num1, num2))
        print("Multiplicación:", multiplicacion(num1, num2))
        
        #Manejar la división
        try:
            print("División:", division(num1, num2))
        except ValueError as e:
            print(f"División: Error - {e}")
            
    except ValueError:
        print("Error: Ingrese números válidos.")
