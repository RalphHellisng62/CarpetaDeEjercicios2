'''
# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta
'''
def juego_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    
    # Solicitar las opciones de los jugadores
    jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
    jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
    
    # Verificar si las opciones son válidas
    if jugador1 not in opciones or jugador2 not in opciones:
        print("Opción incorrecta, por favor elige entre piedra, papel o tijera.")
        return
    
    # Determinar el resultado
    if jugador1 == jugador2:
        resultado = "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        resultado = "Gana Jugador 1"
    else:
        resultado = "Gana Jugador 2"
    
    # Mostrar el resultado
    print(resultado)
    
# Ejecutar el juego
juego_piedra_papel_tijera()