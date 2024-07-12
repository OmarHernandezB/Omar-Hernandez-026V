from funciones import *

sueldos = []

while True:
    print("""[1]Asignar sueldos aleatorios
          [2]Calificar sueldos
          [3]Ver estadísticas
          [4]Reporte de sueldos
          [5]Salir""")
    
    op = int(input("Ingrese el número que desea utilizar: "))

    if op == 1:
        lista_empleados(sueldos)
    if op == 2:
        clasificar_sueldo(sueldos)
    if op == 3:
        ver_estadisticas(sueldos)
    if op == 4:
        reporte_sueldos(sueldos)
    if op == 5:
        print("Finalizando programa")
        print("Desarrollado por Omar Hernandez")
        print("20.882.249-7")
        break