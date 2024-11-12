'''
# Escribe un programa que lea un número e indique si es par o impar.
'''
# Se le pide al usuario que ingrese un número
numero = int(input("Ingrese un número: "))  # Convertimos la entrada a tipo int

# Determinar si el número es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")