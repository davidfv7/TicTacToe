play = True
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

    print("¿Otra partida?")
    another_one= input()
    N
    if(another_one.lower()=="N".lower()):
        play=False