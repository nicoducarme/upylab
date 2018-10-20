def duree(debut, fin):
    D = debut[0]*60 + debut[1]
    F = fin[0]*60 + fin [1]
    if D < F:
        result = F - D
        H = result//60
        M = result % 60
        dur = (H,M)
    else:
        result = 1440 + (F-D)
        H = result//60
        M = result % 60
        dur = (H,M)
    return dur


print (duree((22, 21),(13, 22)))
