def quitar_vocales(cadena):
    resultado = ""

    for i in cadena:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += i
    return resultado

input = input("Ingrese una cadena de texto: ")
sin_vocales = quitar_vocales(input)

print(f"Texto original: {input}")
print(f"Texto sin vocales: {sin_vocales}")