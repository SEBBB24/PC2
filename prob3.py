numerosingres = []
numerospares = []
numerosimpares = []

while True:
    respuesta = input("Responda con mayúsculas, ¿Desea ingresar un número?: ")

    if respuesta == "SI":
        num = int(input("Ingrese el número: "))
        numerosingres.append(num)
    elif respuesta == "NO":
        break
    else:
        print("Por favor, ingrese SI o NO.")

for num in numerosingres:
    if num % 2 == 0:
        numerospares.append(num)
    else:
        numerosimpares.append(num)

print(f"\nNúmeros ingresados: {numerosingres}")
print(f"Cantidad de números pares: {len(numerospares)}")
print(f"Cantidad de números impares: {len(numerosimpares)}")
