from math import sqrt
def dist(p1,p2):
    result = sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    return result
def parallelogramme(p1,p2,p3,p4):
    if abs(dist(p1,p2) - dist(p3,p4))<(10**-7):
        if abs(dist(p1,p4) - dist(p2,p3))<(10**-7):
            perim = (dist(p1,p2)+dist(p1,p4))*2
            return perim
print(parallelogramme((0.0, 2.0),(2.0, 2.0),(2.0, 0.0),(0.0, 0.0)))
