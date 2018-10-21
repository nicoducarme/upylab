a = int(input())
x = int(input())
if a >= 0 and a <= 12:  # si le nombre parié est entre 0 et 12 alors on a misé sur le nombre lui meme
    if a == x:  # si la devinette etait bonne alors renvoyer 12 fois la mise sinon 0
        print("12")
    else:
        print("0")


elif a == 13:   #si le nombre donné est 13 on parie pour un nombre paire
    if (x%2) == 0:  # si le nombre est bel et bien paire alors renvoyer 2 sinon 0
        print("2")
    else:
        print("0")


elif a == 14:   #si le nombre donné est 13 on parie pour un nombre impaire
    if x%2 != 0:    # si le nombre est bel et bien paire alors renvoyer 2 sinon 0
        print("2")
    else:
        print("0")


elif a == 15:   #si le nombre donné est 15 on parie pour une case rouge
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 9 or x == 12:   # si le nombre est bel et bien contenu dans une case rouge alors renvoyer 2 sinon 0
        print("2")
    else:
        print("0")


elif a == 16:   #si le nombre donné est 15 on parie pour une case noire
    if x == 2 or x == 4 or x == 6 or x == 8 or x == 10 or x == 11:  # si le nombre est bel et bien contenu dans une case noire alors renvoyer 2 sinon 0
        print("2")
    else:
        print("0")
