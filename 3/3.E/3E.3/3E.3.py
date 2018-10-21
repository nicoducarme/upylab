n = int(input())
i = 1
for i in range(1,n):
    print(i)


a = 1
while a < n:
    print(a)
    a = a + 1


i = 0
for i in range(0,n+1):
    print(i)


a = 0
while a <= n:
    print(a)
    a = a + 1


i = n
for i in range(n,-1, -1):
    print(i)


a = n
while a >= 0:
    print(a)
    a = a - 1

i = 0
for i in range(0,n+1):
    if i%2 == 0:
        print(i)

a = 0
while a <= n:
    if a%2 == 0:
        print(a)
    a = a + 1


i = 1
for i in range(1,n+1):
    if i%7 == 0:
        print(i)

a = n
while a >= 0:
    if a%5 == 0:
        print(a)
    a = a - 1
