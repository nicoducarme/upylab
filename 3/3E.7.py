n = int(input())
test = False
n1 = 0
n2 = 1
i = 1
result = ("0 1 ")
while test == False:
    n1 = n1 + n2
    i = i + 1
    if i < n:
         result = result + str(n1) + " "
    elif i == n:
        test = True
    n2 = n1 + n2
    i = i + 1
    if i < n:
         result = result + str(n2) + " "
    elif i == n:
        test = True
print(result)
