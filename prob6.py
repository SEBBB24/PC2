fibonacci = [0, 1]

while fibonacci[-1] + fibonacci[-2] <= 50:
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_numero)

print("La serie de Fibonacci hasta el número 50 es: " + str(fibonacci))