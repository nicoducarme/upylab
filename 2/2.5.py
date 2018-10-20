from math import cos, sin, pi
long = float(input())
if long > 0:
    i = 0
    while i < 6:
        x = long* cos(i*(pi)/3)
        y = long* sin(i*(pi)/3)
        print(x,y)
        i = i + 1
