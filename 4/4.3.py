def fibo(n):
    n1 = 0
    n2 = 1
    n3 = 0
    if n < 0:
        print("None")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        print("0")
        print("1")
        for i in range(n-2):
            n1 = n2
            n2 = n2 + n3
            n3 = n1
            print (n2)
        return n2 + n1




n = int(input())

fibo(n)
