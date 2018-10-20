from math import sqrt
def distance_points(p1,p2):
    result = sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    return result
def longueur(*points):
    n = len(points)
    sum = 0
    for i in range(n-1):
        sum += distance_points(points[i],points[i+1])
    return sum
