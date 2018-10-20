from math import sqrt
def distance_points(p1,p2):
    result = sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    return result
