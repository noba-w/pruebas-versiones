def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Introduce un número entero: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        print(f"El factorial de {numero} es {factorial(numero)}")
except ValueError:
    print("Por favor, introduce un número entero válido.")