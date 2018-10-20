import random
def alea_dice(s):
    random.seed(s)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d1,d2,d3 = sorted([d1,d2,d3], reverse= True)
    resultat = d1*100 + d2*10 +d3
    if resultat == 421:
        return True
    else:
        return False
