det = int(input())
test = True
data = 0
total = 0
if det >=  0:
    for i in range(det):
        data = int(input())
        total = total + data
else :
    while test == True:
        data = input()
        if data == "F":
            test = False
        else:
            total = total + int(data)

print(total)
