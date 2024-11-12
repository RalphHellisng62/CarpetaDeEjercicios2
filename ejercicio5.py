'''
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

'''

# Escribe el nombre de usuario
usuario = input("Introduce tu nombre de usuario: ")

# Crea la contraseña
contrasena = input("Introduce tu contraseña: ")

# Verificar las credenciales
if usuario == "pepe" and contrasena == "asdasd":
    print("Has entrado al sistema.")
else:
    print("Error: Nombre de usuario o contraseña incorrectos.")