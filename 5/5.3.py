def plus_grand_bord(w):
    n = len(w)
    bord = ""
    i = 0
    for i in range(n):
        if w[0:i] == w[-i:]:
            bord = w[0:i]
    return bord
