# Pide números al usuario hasta que escriba -1 .
# Al final muestra cuál fue el mayor número ingresado

mayor = 0
result = 0

while True:
    number = int(input("Ingrese un número: "))
    if number != -1:
        if number > mayor:
            mayor = number
    else:
        print(f"El número mayor es {mayor}")
        break