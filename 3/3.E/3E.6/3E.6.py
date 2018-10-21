n = int(input())
n1 = 0
n2 = 1
result = (str(0) + " " + str(1) + " ")
while (n1+n2) < n and n2 < n:
    n1 = n1 + n2
    n2 = n1 + n2
    if n1 < n and n2 < n:
        result = result + (str(n1) +" "+ str(n2) + " ")
    if n1 < n and n2 > n:
         result = result + (str(n1))
print(result)
