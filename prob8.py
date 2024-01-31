def factorial_recursivo(num):
    # Factorial de 0 es 1
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num - 1)

num = int(input("Ingrese un número entero no negativo: "))

resultado_factorial = factorial_recursivo(num)

print(f"El factorial de {num} es: {resultado_factorial}")
