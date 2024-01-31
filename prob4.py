def ingresar_datos_alumno():
    alumno = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera calificación: "))
    nota2 = float(input("Ingrese la segunda calificación: "))
    nota3 = float(input("Ingrese la tercera calificación: "))

    return {"Alumno": alumno, "Notas": [nota1, nota2, nota3]}

def mostrar_listado_alumnos(listado):
    print("\nListado de Alumnos:")
    for alumno in listado:
        print(f"{alumno['Alumno']} - Calificaciones: {alumno['Notas']}")

listado_alumnos = []
while True:
    alumno = ingresar_datos_alumno()
    listado_alumnos.append(alumno)

    continuar = input("¿Desea ingresar otro alumno? (SI/NO): ").upper()
    if continuar != "SI":
        break
(listado_alumnos)
