from math import sqrt


def droite(p1,p2):
    if p1[0] != p2[0]:
        a = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p1[1]-a*p1[0]
        return (a,b)

def appartient(d,p):
    app = False
    if  p[1] == d[0]*p[0]+d[1]:
        app = True
    return app


def coefficient_angulaire(d):
    a = d[0]
    return a


def intersection_abscisses(d):
    x = (-d[1])/d[0]
    return (x,0)


def paralleles(d1,d2):
    par = False
    if d1[0] == d2[0]:
        par = True
    return par


def confondues(d1,d2):
    conf = False
    if d1[0] == d2[0] and d1[1] == d2[1]:
        conf = True
    return conf


def intersection(d1,d2):
    inter = tuple()
    if confondues(d1,d2) == True:
        x = 0
        y = d1[1]
        inter = (x,y)
    elif paralleles(d1,d2) == True:
        inter = None
    else:
        x = (d2[1] - d1[1])/(d1[0] - d2[0])
        y = d1[0]*x + d1[1]
        inter = (x,y)
    return inter


def droite_normale(d, p):
    a = -(d[0]**-1)
    b = p[1] + p[0]/d[0]
    return (a,b)


def droite_parallele(d, p):
    a = d[0]
    b = p[1] - (d[0] * p[0])
    return (a,b)


def distance_droite(d, p):
    dnor = droite_normale(d,p)
    pinter = intersection(dnor, d)
    dist = sqrt((p[0]-pinter[0])**2+(p[1]-pinter[1])**2)


def symetrie_orthogonale(d, p):
    dnor = droite_normale(d,p)
    pinter = intersection(dnor, d)
    x = p[0]+2*(pinter[0]-p[0])
    y = p[1]+2*(pinter[1]-p[1])
    return(x,y)
