def duree(debut, fin):
    D = debut[0]*60 + debut[1]
    F = fin[0]*60 + fin[1]
    test = 1440*int(D>F)
    result = abs(test- abs(D-F))
    H = result//60
    M = result % 60
    dur = (H,M)
    return dur
