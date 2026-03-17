# El programa muestra un menú con varias opciones.
# El usuario elige una operación y el programa la ejecuta.
# Se usa:
# for para repetir varias veces,
# match para seleccionar la operación
# if para validar entradas.

def suma(a, b):
    suma = a + b
    return suma

def resta(a, b):
    resta = a - b
    return resta

def multiplicacion(a, b):
    multiplicacion = a * b
    return multiplicacion

def division(a, b):
    if b != 0:
        division = a / b
        return division
    else:
        return f"No se puede dividir por cero. {a}/{b}"

def div_entera(a, b):
    if b != 0:
        div_entera = a // b
        return div_entera
    else:
        return f"No se puede dividir por cero. {a}/{b}"

def potencia(a, b):
    potencia = pow(a, b)
    return potencia

def modulo(a, b):
    if b != 0:
        modulo = a % b
        return modulo
    else:
        return f"No se puede dividir por cero. {a}/{b}"

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el primer numero: "))

menu = """
==== Calculadora ====

Escoja una opcion:
1. Suma
2. Resta
3. Multiplicación
4. Division
5. Division parte entera
6. Potencia
7. Módulo
8. Salir

"""

for opcion in range(1000):
    print(menu)
    option = int(input("Escoja una opción: "))
    
    match option:
        case 1:
            print(f"El total de la suma es {suma(a, b)}")
        case 2:
            print(f"El resultado de la resta es {resta(a, b)}")
        case 3:
            print(f"El resultado de la multiplicaión es {multiplicacion(a, b)}")
        case 4:
            print(f"El resultado de la división es {division(a,b)}")
        case 5:
            print(f"El resultado de la division entera es {div_entera(a,b)}")
        case 6:
            print(f"El resultado de la potencia es {potencia(a,b)}")
        case 7:
            print(f"El resultado de el modulo es {modulo(a,b)}")
        case 8:
            print(f"Gracias por utilizar nuestra calculadora.")
            break
        