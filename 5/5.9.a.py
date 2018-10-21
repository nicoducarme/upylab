def bornes(nombres):
    long = len(nombres)
    if long != 0 and long != 1:
        n1 = nombres[0]
        n2 = nombres[1]
        for i in range(long-1):
            if n1 < n2:
                min = n1
            else:
                min = n2
            n1 = min
            if i != long-2:
                n2 = nombres[i+2]
        n1 = nombres[0]
        n2 = nombres[1]
        for j in range(long-1):
            if n1 > n2:
                max = n1
            else:
                max = n2
            n1 = max
            if j != long-2:
                n2 = nombres[j+2]
    elif long == 1:
        min, max = 0,0
    return (min,max)
