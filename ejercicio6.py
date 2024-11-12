'''
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

'''
# Programa que verifica si una cadena es una letra mayúscula
def es_mayuscula(cadena):
    if len(cadena) == 1 and cadena.isupper():
        return True
    return False

# Leer una cadena por teclado
entrada = input("Introduce una letra: ")

# Comprobar si es una letra mayúscula
if es_mayuscula(entrada):
    print(f"{entrada} es una letra mayúscula.")
else:
    print(f"{entrada} no es una letra mayúscula.")