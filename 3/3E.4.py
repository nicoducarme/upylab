a = int(input())
b = int(input())
c = a%b
if b >a:
    a,b = b,a
test = True
pr = False
if c == 0:
    test = False
    pr = False
elif c == 1:
    test = False
    pr = True
elif c == a:
    test = False
    pr = True
while test == True:
    if (a%c) == 1:
        test = False
        pr = True
    elif(a%c == 0):
        test = False
        pr = False
    else:
        c = a%c
if pr:
    print("OK")
else:
    print("KO")
