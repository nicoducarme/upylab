def premier(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2,n):
            k = test(i)
            if k == 0:
                print(i)
        return test(n) == 0

def test(i):
    for b in range(2,int(i/2)+1):
        if i%b == 0:
            return 1
    return 0
n = int(input())
premier(n)
