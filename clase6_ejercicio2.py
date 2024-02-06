import random

while True:
    aleatorio = random.randrange(0,3)
    elijePC = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. tijera")
    opcion = int(input("Elije tu opcion:  "))

    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print ("Elejiste: ", elijeUsuario)

    if aleatorio == 0:
        elijePC = "Piedra"
    elif aleatorio == 1:
        elijePC = "Papel"
    elif opcion == 3:
        elijePC = "Tijera"
    print("La maquina elijio: ", elijePC)
    print("...")
    if elijePC == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste, papel envuelve Piedra, asi se hace")
    elif elijePC == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta papel, asi se hace,")
    elif elijePC == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste piedra machaca Tijera, asi se hace")
    if elijePC == "Papel" and elijeUsuario == "Piedra":
        print("Perdiste Papel envuelve a Piedra, hazlo mejor la proxima")
    elif elijePC == "Tijera" and elijeUsuario == "Papel":
        print("perdiste, Tijera corta Papel, hazlo mejor la proxima")
    elif elijePC == "Piedra" and elijeUsuario == "Tijera":
        print("perdiste, Piedra machaca Papel, hazlo mejor la proxima")
    elif elijePC == elijeUsuario:
        print("empate")
