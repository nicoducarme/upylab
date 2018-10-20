def anagrammes(v, w):
    if sorted(v) == sorted(w):
        con = True
    else:
        con = False
    return con
