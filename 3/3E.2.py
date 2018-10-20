n = int(input())
i = 0
while i < n//2:
    print( (i*"X")+ ("O")+((n-2-(2*i))*"X") + ("O") + (i*"X"))
    i = i +1
mil = int((n-1)/2)
i = i-1
print(mil*"X" + "O" + mil*"X")
while i >= 0:
    print( (i*"X")+ ("O")+((n-2-(2*i))*"X") + ("O") + (i*"X"))
    i = i -1
