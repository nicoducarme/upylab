n = int(input())
i = 0
#premiere moitié du carré
while i < n//2:
    print( (i*"X")+ ("O")+((n-2-(2*i))*"X") + ("O") + (i*"X"))
    i = i +1
mil = int((n-1)/2)
i = i-1
#ligne du milieu
print(mil*"X" + "O" + mil*"X")
#deuxieme moitié du carré
while i >= 0:
    print( (i*"X")+ ("O")+((n-2-(2*i))*"X") + ("O") + (i*"X"))
    i = i -1
