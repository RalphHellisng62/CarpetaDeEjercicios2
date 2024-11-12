'''
# Programa que pida dos números e indique Cuál es el mayor
# Si los dos son iguales que muestre el mensaje "Son iguales"
'''
# Se le pide al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Comparar los números e imprimir el resultado
if num1 > num2:
    print("El número mayor es: {num1}")
elif num2 > num1:
    print("El número mayor es: {num2}")
else:
    print("Los numeros son iguales")