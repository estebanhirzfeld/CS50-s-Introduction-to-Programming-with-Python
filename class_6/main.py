import csv

def agregar_estudiante(nombre, apellido, nacimiento):
    with open('estudiantes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, apellido, nacimiento])

agregar_estudiante('Lucia', 'Garcia', '10/06/2003')
agregar_estudiante('Joaquin', 'Torres', '22/04/1996')
agregar_estudiante('Emilia', 'Gutierrez', '17/09/2001')

# #borrar archivo por coincidencia exacta
# def borrar_estudiante(nombre, apellido, nacimiento):
#     with open('estudiantes.csv', 'r') as file:
#         lines = file.readlines()
#     with open('estudiantes.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         for line in lines:
#             if line.strip() != f"{nombre},{apellido},{nacimiento}":
#                 writer.writerow(line.strip().split(','))



# borrar_estudiante('Lucia', 'Garcia', '10/06/2003')
# borrar_estudiante('Joaquin', 'Torres', '22/04/1996')
# borrar_estudiante('Emilia', 'Gutierrez', '17/09/2001')
