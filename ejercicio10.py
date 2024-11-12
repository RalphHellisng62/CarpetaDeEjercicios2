'''
#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un programa que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.

'''
# Programa para calcular el costo del viaje con funciones
def costo_por_alumno(num_alumnos):
    if num_alumnos >= 100:
        return 65
    elif num_alumnos >= 50:
        return 70
    elif num_alumnos >= 30:
        return 95
    else:
        return None  # Para el caso de menos de 30 alumnos

def calcular_pago(num_alumnos):
    costo = costo_por_alumno(num_alumnos)
    if costo is None:  # Menos de 30 alumnos
        total_pago = 4000
        costo = total_pago / num_alumnos
    else:
        total_pago = costo * num_alumnos
    return total_pago, costo

# Solicitar entrada al usuario
num_alumnos = int(input("Introduce el número de alumnos: "))

# Calcular el pago y el costo por alumno
total_pago, costo = calcular_pago(num_alumnos)

# Mostrar resultados
if num_alumnos < 30:
    print(f"El costo total es: {total_pago} euros.")
    print(f"Cada alumno debe pagar: {costo:.2f} euros.")
else:
    print(f"El costo total a pagar a la compañía es: {total_pago} euros.")
    print(f"Cada alumno debe pagar: {costo} euros.")