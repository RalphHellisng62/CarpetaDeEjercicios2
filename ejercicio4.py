'''
Crea un programa que pida al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrario.

'''
# Se le pide al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))  # Convertimos la entrada a tipo float
num2 = float(input("Ingrese el segundo número: "))  # Convertimos la entrada a tipo float

# Verificar si el segundo número es cero
if num2 != 0:
    division = num1 / num2
    print(f"La división de {num1} entre {num2} es: {division}")
else:
    print("Error: No se puede dividir por cero.")