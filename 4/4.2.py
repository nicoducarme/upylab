from math import factorial
e = 10**(-6)
def sin(x):
    somme = 0
    i = 0
    while abs((x**((2*i)+1))/(factorial((2*i)+1))) > e:
        somme = somme + ((-1)**i)*(x**((2*i)+1))/(factorial((2*i)+1))
        i = i + 1
    return somme
a = float(input())
print(sin(a))
