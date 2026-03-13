# Pide un número y usa  para imprimir su tabla de multiplicar del 1 al 10.
# Ejemplo: si el número es 7 → imprime 7×1, 7×2, …, 7×10.

tabla = int(input("Introduce un numero: "))
i = 1

while i < 11:
    print(f"{i} * {tabla} = {i * tabla}")
    i += 1