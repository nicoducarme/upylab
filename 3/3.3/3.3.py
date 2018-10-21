a = int(input())
b = int(input())
c = int(input())
if c == 1:  #si c = 1
    print(a+b)
elif c==2:  #sinon si c = 2
    print(a-b)
elif c==3:  #sinon si c = 3
    print(a*b)
elif c==4: #sinon si c = 4
    print((a**2)+(b*a))
else: print("Erreur") #si aucune des condition precedentes n'est vraies, executer ceci
