a = int(input())
x = int(input())
if a >= 0 and a <= 12:
    if a == x:
        print("12")
    else:
        print("0")


elif a == 13:
    if (x%2) == 0:
        print("2")
    else:
        print("0")


elif a == 14:
    if x%2 != 0:
        print("2")
    else:
        print("0")


elif a == 15:
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 9 or x == 12:
        print("2")
    else:
        print("0")


elif a == 16:
    if x == 2 or x == 4 or x == 6 or x == 8 or x == 10 or x == 11:
        print("2")
    else:
        print("0")


else :
    print("erreur")
