play = True
#funciones que asignan la posicion y el jugador
def setPositionA0():
    return (0,0)
def setPositionA1():
    
    return (0,1)
def setPositionA2():
    return (0,2)
def setPositionB0():
    return (1,0)
def setPositionB1():
   
    return (1,1)
def setPositionB2():
    
    return (1,2)
def setPositionC0():
    
    return (2,0)
def setPositionC1():
    
    return (2,1)
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
    positions= [["","",""],["","",""],["","",""]]
    p1 = "P1"
    p2 = "P2"
    actualplayer=p1
    print("Instrucciones:")
    print("A ---- B ---- C  ")
    
    while(True):
        print("%s move:" % actualplayer)
        option = input()
        moveCases(option,positions,actualplayer)
        print(positions)
        if(actualplayer=="P1"):
            actualplayer = "P2"
        else:
            actualplayer="P1"
    
    

    

    print("¿Otra partida?")
    another_one= input()
    
    if(another_one.lower()=="N".lower()):
        play=False