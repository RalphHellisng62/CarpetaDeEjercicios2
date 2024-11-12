'''
# Realiza un programa que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

'''
# Programa para calcular la potencia
def calcular_potencia(base, exponente):
    if exponente > 0:
        return base ** exponente
    elif exponente == 0:
        return 1
    else:  # exponente negativo
        return 1 / (base ** abs(exponente))

# Leer base y exponente por teclado
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calcular y mostrar el resultado
resultado = calcular_potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}.")