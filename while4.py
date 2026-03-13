# Pide un número entero y usa while para invertirlo.
# Ejemplo: 1234 → 4321.

number = int(input("Ingrese un número: "))

inverted = 0

while number > 0:
    digit = number % 10
    inverted = inverted * 10 + digit
    number = number // 10
print(f"El numero invertido es: {inverted}")