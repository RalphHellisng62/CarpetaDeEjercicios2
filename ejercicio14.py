'''
#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
'''
def dias_del_mes(mes):
    if mes == 1:   # Enero
        return 31
    elif mes == 2: # Febrero
        return 28  # Sin contar los años bisiestos
    elif mes == 3: # Marzo
        return 31
    elif mes == 4: # Abril
        return 30
    elif mes == 5: # Mayo
        return 31
    elif mes == 6: # Junio
        return 30
    elif mes == 7: # Julio
        return 31
    elif mes == 8: # Agosto
        return 31
    elif mes == 9: # Septiembre
        return 30
    elif mes == 10: # Octubre
        return 31
    elif mes == 11: # Noviembre
        return 30
    elif mes == 12: # Diciembre
        return 31
    else:
        raise ValueError("Número fuera del rango (1-12)")

# Solicitar al usuario que introduzca un número
try:
    mes = int(input("Introduce un número entero entre 1 y 12: "))
    dias = dias_del_mes(mes)
    print(f"El mes {mes} tiene {dias} días.")
except ValueError as e:
    print(e)