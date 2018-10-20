from math import sqrt
def rac_eq_2nd_deg(a,b,c):
    if (b**2)-4*a*c < 0:
        sol = tuple()
    elif (b**2)-4*a*c == 0:
        r1 = (-b + sqrt((b**2)-4*a*c))/2
        sol = (r1,)
    else:
        r1 = (-b + sqrt((b**2)-4*a*c))/(2*a)
        r2 = (-b - sqrt((b**2)-4*a*c))/(2*a)
        sol = (min(r1,r2), max(r1,r2))
    return sol
