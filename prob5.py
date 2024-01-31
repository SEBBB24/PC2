def contar_digitos(numero, digito):
    str_numero = str(numero)

    cantidad = str_numero.count(str(digito))
    
    return cantidad

numero_ingresado = int(input("Ingrese un número entero: "))
digito_a_contar = int(input("Ingrese un dígito: "))

cantidad_apariciones = contar_digitos(numero_ingresado, digito_a_contar)

print(f"Cantidad de veces que aparece {digito_a_contar} en el número {numero_ingresado}: {cantidad_apariciones}")