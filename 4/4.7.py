def rendre_monnaie(prix,tup):
    donne = 20*tup[0]+10*tup[1]+5*tup[2]+2*tup[3]+tup[4]
    if donne < prix:
        return None
    else:
        reste = donne - prix
        y20 = reste // 20
        reste = reste - (y20 * 20)
        y10 = reste // 10
        reste = reste - (y10 * 10)
        y5 = reste // 5
        reste = reste - (y5 * 5)
        y2 = reste // 2
        reste = reste - (2 * y2)
        y1 = reste
        tup2 = (y20,y10,y5,y2,y1)
        return  tup2
