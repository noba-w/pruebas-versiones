import random

numero_secreto = random.randint(1, 5)
intento = input("Adivina el número (entre 1 y 5): ")

try:
    intento = int(intento)
    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
    else:
        print(f"Incorrecto. El número era {numero_secreto}.")
except ValueError:
    print("Por favor, introduce un número entero válido.")