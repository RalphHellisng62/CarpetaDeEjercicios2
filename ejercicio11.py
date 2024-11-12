'''
#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.
'''

import datetime

def calcular_costo_llamada(duracion, dia_semana, hora):
    # Costo base según la duración
    if duracion <= 5:
        costo = 1.0
    elif duracion <= 8:
        costo = 1.0 + 0.80
    elif duracion <= 10:
        costo = 1.0 + 0.80 + 0.70
    else:
        costo = 1.0 + 0.80 + 0.70 + (duracion - 10) * 0.50

    # Cálculo del impuesto
    if dia_semana == 'domingo':
        impuesto = 0.03  # 3%
    else:
        if hora < 12:  # Turno de mañana
            impuesto = 0.15  # 15%
        else:  # Turno de tarde
            impuesto = 0.10  # 10%

    # Cálculo del total
    total = costo + (costo * impuesto)
    return costo, impuesto, total

# Leer datos de entrada
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana (ej. domingo, lunes, martes...): ").strip().lower()
hora = int(input("Introduce la hora de la llamada en formato 24 horas (0-23): "))

# Verificar día de la semana
dias_validos = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
if dia not in dias_validos:
    print("Día de la semana no válido. Por favor, introduce un día válido.")
else:
    costo, impuesto, total = calcular_costo_llamada(duracion, dia, hora)
    
    # Mostrar resultados
    print(f"\nCosto de la llamada: {costo:.2f} euros")
    print(f"Impuesto aplicado: {impuesto * 100:.2f}%")
    print(f"Total a pagar: {total:.2f} euros")