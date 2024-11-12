'''
#Programa que pida tres números y los muestre ordenados (de mayor a menor);
'''
# Programa que ordena tres números de mayor a menor sin usar listas
# Leer tres números por teclado
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Determinar el orden de los números
if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1
else:
    mayor = num3
    if num1 >= num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1

# Mostrar los números ordenados
print("Los números ordenados de mayor a menor son:", mayor, medio, menor)