'''
# Programa que pida un número y diga si es positivo, negativo o 0.

'''
# Se le pide al usuario que ingrese un número
num = float(input("Ingrese un número: "))  # Convertimos la entrada a tipo float

# Determinar si el número es positivo, negativo o cero
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")