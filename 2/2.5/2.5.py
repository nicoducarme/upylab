from math import cos, sin, pi
long = float(input()) #longueur de rayon
for i in range(6) #pour chacun des 6 sommets
    x = long* cos(i*(pi)/3)
    y = long* sin(i*(pi)/3)
    print(x,y)
