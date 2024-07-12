import random
import csv

def lista_empleados(sueldos):
    nom = input("Ingrese el nombre del empleado: ")
    sueldo_bruto = round(random.randint(300000,2500000))
    desct_afp = int(sueldo_bruto * 0.07)
    desct_salud = int(sueldo_bruto * 0.12)
    sueldo_liquido = int(sueldo_bruto - (desct_afp+desct_salud))
    empleado = {"nombre":nom,
             "sueldo bruto":sueldo_bruto,
             "AFP":desct_afp,
             "salud":desct_salud,
             "sueldo liquido":sueldo_liquido,
             }
    sueldos.append(empleado)
    print(f"El empleado {nom} ha quedado con el sueldo {sueldo_bruto}")


def clasificar_sueldo(sueldos):
    clasificacion = {
        "Bajo": [empleado for empleado in sueldos if empleado ["sueldo bruto"]<800000],
        "Medio": [empleado for empleado in sueldos if 800000 <= empleado ["sueldo bruto"]<2000000],
        "Alto": [empleado for empleado in sueldos if empleado["sueldo bruto"]>=2000000]
    }

    for nivel,lista in clasificacion.items():
        print(f"{nivel}:{[( empleado["nombre"],empleado["sueldo bruto"])for empleado in lista]}")

    suma = int(sum(empleado["sueldo bruto"]for empleado in sueldos))
    print(f"La suma de todos los sueldos es: {suma}")

def ver_estadisticas(sueldos):
    promedio = int(sum(empleado["sueldo bruto"] for empleado in sueldos))
    print(f"El promedio de sueldos en la planilla es de: {promedio}/{len(sueldos)}")
    print(f"La media geometrica de la planilla es: {promedio}/{len(sueldos)}")

def reporte_sueldos(sueldos,filename="reporte_sueldos.csv"):
    if sueldos:
        keys = sueldos[0].keys()
        with open(filename,'w',newline='')as output_file:
            sueldo_emp = csv.DictWriter(output_file,fieldnames = keys)
            sueldo_emp.writeheader()
            sueldo_emp.writerows(sueldos)
        print(f"Los Sueldos fueron guardados en la lista {filename}")
    else:
        print("No hay productos para guardar")