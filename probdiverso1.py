def cargar_alumnos(n):
    listado_alumnos = []

    for _ in range(n):
        nombre_completo = input("Ingrese el nombre completo del alumno: ")
        notas = []

        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {i} (entre 0 y 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Por favor, ingrese una nota válida entre 0 y 10.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

        listado_alumnos.append({"Nombre": nombre_completo, "Notas": notas})

    return listado_alumnos

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos a cargar: "))
listado_final = cargar_alumnos(cantidad_alumnos)

print("\nListado de Alumnos:")
for alumno in listado_final:
    print(f"{alumno['Nombre']} - Notas: {alumno['Notas']}")
