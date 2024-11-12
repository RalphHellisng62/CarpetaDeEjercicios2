'''
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".
'''
# Función para obtener el número en letras de la cara opuesta del dado
def cara_opuesta(num):
    opuestas = {
        1: "seis",
        2: "cinco",
        3: "cuatro",
        4: "tres",
        5: "dos",
        6: "uno"
    }
    return opuestas.get(num)

# Solicitar al usuario que introduzca el resultado del dado
resultado = int(input("Introduce el resultado del dado (número del 1 al 6): "))

# Comprobar si el número está dentro del rango válido
if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    letra_opuesta = cara_opuesta(resultado)
    print(f"La cara opuesta al {resultado} es {letra_opuesta}.")
