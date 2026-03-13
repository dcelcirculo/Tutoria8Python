# Pide al usuario ingresar notas (entre 0 y 5).
# El ciclo termina cuando el usuario escribe -1.
# Al final calcula y muestra el promedio de las notas ingresadas

contador = 0
result = 0
while True:
    nota = int(input("Ingrese la nota entre 0 - 5: "))
    if nota != -1:
        result += nota
        contador += 1
    else:
        promedio = result / contador
        print(f"Su promedio es {promedio}")
        break