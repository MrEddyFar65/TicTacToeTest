
import random

#Programar TicTacToe intento N.02

#Variables y/o listas
board = [1,2,3,4,5,6,7,8,9]

in_game = True

tiro_cpu = True
#nombre de los jugadores
jugador = input("Favor de ingresar tu nombre de jugador (X):")


#Tablero del juego
def Board():
    print(f"   {board[0]}   |    {board[1]}   |   {board[2]}")
    print("-" * 25)
    print(f"   {board[3]}   |    {board[4]}   |   {board[5]}")
    print("-" * 25)
    print(f"   {board[6]}   |    {board[7]}   |   {board[8]}")


#Turno del Jugador
def tiroJugador(variable):

    tiro_aceptado = True

    #Chequeo de tiro valido
    while tiro_aceptado:
        tiro = int(input(f"{variable} elige una casilla: "))
        
        if tiro <= 0 or tiro >=10 or board[tiro - 1] == "X" or board[tiro - 1] == "O":
            print("Tiro no aceptado\n Rango de tiro invalido o casilla ocupada")
        else:
            tiro_aceptado = False   

    board[tiro-1] = "X"


#Turno del CPU 
def tiroCPU():
    tiro_aceptado_cpu = True
    i = 0
    global in_game

    """Ciclo For 
    Conteo de casillas ocupadas para decision de tablas"""
    for n in board:
        if n == "X" or n == "O":
            i += 1
        else:
            continue

    if i == 9:
        print("Las casillas se han terminado, el juego ha quedado: \n Empatado!!! ")
        in_game = False
        tiro_aceptado_cpu = False
        return in_game     
    
    
    """Tiro del CPU
    Comentario: Funcionamiento random, no hay ventaja en decision de la maquina"""
    while tiro_aceptado_cpu:
        tiro_cpu = random.randint(0,8)

        if board[tiro_cpu] == 'X' or board[tiro_cpu] == "O":
            print("mal")
        else:
            tiro_aceptado_cpu = False
    
 
    board[tiro_cpu] = "O"


#Ganador del juego
def ganador_game():

    jugado_x = "X"
    jugador_0 = "O"
    global in_game
    
    #En Horizontal
    if board[0] == board[1] == board[2] and board[0] == "X" or board[3] == board[4] == board[5] and board[3] == "X" or board[6] == board[7] == board[8] and board[6] == "X":
        print("_"*30)
        print(f"Felicidades ha ganado {jugador}")
        print("_"*30)
        in_game = False

        return in_game
    elif board[0] == board[1] == board[2] and board[0] == "O" or board[3] == board[4] == board[5] and board[3] == "O" or board[6] == board[7] == board[8] and board[6] == "O":
        print("_"*30)
        print("Ha ganado el CPU")
        print("_"*30)
        in_game = False

        return in_game
    
    #En Vertical
    elif board[0] == board[3] == board[6] and board[0] == "X" or board[1] == board[4] == board[7] and board[1] == "X" or board[2] == board[5] == board[8] and board[2] == "X":
        print("_"*30)
        print(f"Felicidades ha ganado {jugador}")
        print("_"*30)
        in_game = False

        return in_game
    elif board[0] == board[3] == board[6] and board[0] == "O" or board[1] == board[4] == board[7] and board[1] == "O" or board[2] == board[5] == board[8] and board[2] == "O":
        print("_"*30)
        print("Ha gando el CPU")
        print("_"*30)
        in_game = False
        return in_game

    #En Cruz
    elif board[0] == board[4] == board[8] and board[0] == "X" or board[2] == board[4] == board[6] and board[2] == "X":
        print("_"*30)
        print(f"Felicidades ha ganado {jugador}")
        print("_"*30)
        in_game = False 
        return in_game
    elif board[0] == board[4] == board[8] and board[0] == "O" or board[2] == board[4] == board[6] and board[2] == "O":
        print("_"*30)
        print("Ha ganado el CPU")
        print("_"*30)
        in_game = False 
        return in_game
     





#TIC TAC TOE
while in_game:
    Board()
    tiroJugador(jugador)
    tiroCPU()
    ganador_game()
    
Board()  


