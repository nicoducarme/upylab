def test(i):
    for b in range(2,int(i/2)+1):
        if i%b == 0:
            return 1
    return 0
def prime_numbers(t):
    i = 0
    j = 2
    ok = True
    liste= []
    if isinstance(t,int):
        if t >= 0 and isinstance(t,int):
            while i < t:
                while ok == True:
                    if test(j) == 0:
                        liste.append(j)
                        i+=1
                        j+=1
                        if i == t:
                            ok = False
                    else:
                        j+=1
            return liste
        elif t<0:
            return None
