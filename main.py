import numpy as np
play = True
board=[i for i in range(0,9)]

print(board)
#Funcion para evaluar si el tablero esta lleno
def is_board_full(positions):
    full = True
    plainPositions = [i for pos in positions for i in pos]
    for i in plainPositions:
        if(i ==''):
            full = False
            break
    return full
    
#Funcion para evaluar victoria o empate
def check_win(positions,player):
    checkList = [pos for pos in positions]
    win = True
    
    winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for tup in winners:
        win=True
        for x in tup:
           
            if(positions[x]!=player):
                
               
                win=False
                break
       
        if(win==True):
            
            break
    return win


def is_match_over(positions,player):
    plainPositions = [i for pos in positions for i in pos]
    match = check_win(plainPositions,player)
    
    return match



#funciones que asignan la posicion y el jugador
def setPositionA0():
    return (0,0)
def setPositionA1():
    
    return (1,0)
def setPositionA2():
    return (2,0)
def setPositionB0():
    return (0,1)
def setPositionB1():
   
    return (1,1)
def setPositionB2():
    
    return (2,1)
def setPositionC0():
    
    return (0,2)
def setPositionC1():
    
    return (1,2)
def setPositionC2():
    return(2,2)
# Funcion que evalua la opcion
def moveCases(option,positions,player):
    option = option.upper()
    print(option)
    switcher= {
        "A0": setPositionA0(),
        "A1": setPositionA1(),
        "A2": setPositionA2(),
        "B0": setPositionB0(),
        "B1": setPositionB1(),
        "B2": setPositionB2(),
        "C0": setPositionC0(),
        "C1": setPositionC1(),
        "C2": setPositionC2(),

    }
    
    pos = switcher.get(option, "Invalid option")
    positions[pos[0]][pos[1]] = player
    
 


while(play):

    print(".................JUEGO DEL GATO...........................\n"
          "Instrucciones:                                            \n"
          "   1. Observa la siguiente matriz                         \n"
          "             A     B      C                               \n"
          "                |     |                                   \n"
          "        0   ____|_____|____                               \n"
          "                |     |                                   \n"
          "        1   ____|_____|____                               \n"
          "                |     |                                   \n"
          "        2       |     |                                   \n"
          "                                                          \n"
          "   2. Coloca la posición de tu jugada mediante coordenadas\n"
          "      como (A,0) o (C,2)                                  \n"
          "                                                          \n")
    print("-------------::::COMIENZA EL JUEGO::::--------------------\n")

    positions= [["","",""],["","",""],["","",""]]
    p1 = "X"
    p2 = "O"
    actualplayer=p1
    winner=False
    while(winner==False):
       
        while(is_board_full(positions)==False ):
            print("%s move:" % actualplayer) 
            option = input()
            moveCases(option,positions,actualplayer)
            print(np.array(positions))
            
            if(is_match_over(positions,actualplayer)==True ):
                print("El ganador es: ",actualplayer)
                winner=True
                break
            if(actualplayer=="X"):
                actualplayer = "O"
            else:
                actualplayer="X"
        if(is_board_full(positions)==True):
            print( "¡¡EMPATE!!")
            winner=True

    print("¿Otra partida?")
    another_one= input()
    
    if(another_one.lower()=="N".lower()):
        play=False