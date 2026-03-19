# Pedir al usuario un número
numero = int(input("Ingrese un número: "))

# Inicializar una lista para almacenar los divisores
divisores = []

# Encontrar los divisores
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Mostrar los divisores
print("Los divisores de", numero, "son:", divisores)
