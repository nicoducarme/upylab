from math import sqrt
nom = str(input())
a = float(input())
if nom == "T" or nom == "C" or nom == "O" or nom == "D" or nom == "I":
    if nom == "T":
        print(((a**3)*sqrt(2))/12)
    elif nom == "C":
        print(a**3)
    elif nom == "O":
        print(((a**3)*sqrt(2))/3)
    elif nom == "D":
        print(((a**3)*(15+7*sqrt(5)))/4)
    elif nom == "I":
        print(((a**3)*(15+5*sqrt(5)))/12)
else:
    print("Polyèdre non connu")
