import random
NB_ESSAIS_MAX = 6
secret = random.randint(0,100)
i = 0
test = True
while test == True:
    i = i +1
    if i < NB_ESSAIS_MAX+1:
        a = int(input())
        if a == secret:
            print("Gagné en ",i," essais !")
            test = False
        elif a > secret and i != NB_ESSAIS_MAX:
            print("Trop grand")
        elif a < secret and i != NB_ESSAIS_MAX:
            print("Trop petit")
    else:
        test = False
        print("Perdu !")
