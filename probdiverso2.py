def evaluar_aprobacion(listado_alumnos):
    aprobados = sum(1 for alumno in listado_alumnos if sum(alumno['Notas']) / len(alumno['Notas']) >= 4)
    desaprobados = len(listado_alumnos) - aprobados

    return aprobados, desaprobados

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos a cargar: "))
listado_final = cargar_alumnos(cantidad_alumnos)

print("\nListado de Alumnos:")
for alumno in listado_final:
    print(f"{alumno['Nombre']} - Notas: {alumno['Notas']}")

aprobados, desaprobados = evaluar_aprobacion(listado_final)

print("\nResultados de Evaluación:")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
