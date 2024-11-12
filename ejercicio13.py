'''
#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.
'''
def dia_de_la_semana():
    # Definimos una lista con los días de la semana
    dias = [
        "Lunes",    # 1
        "Martes",   # 2
        "Miércoles",# 3
        "Jueves",   # 4
        "Viernes",  # 5
        "Sábado",   # 6
        "Domingo"   # 7
    ]

    # Pedimos al usuario que introduzca un número del 1 al 7
    try:
        dia_numero = int(input("Introduce un número del 1 al 7 para obtener el día de la semana: "))

        # Validamos el número introducido
        if 1 <= dia_numero <= 7:
            # Imprimimos el día correspondiente
            print(f"El día correspondiente es: {dias[dia_numero - 1]}")
        else:
            print("Error: El número debe estar entre 1 y 7.")
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

# Llamamos a la función
dia_de_la_semana()