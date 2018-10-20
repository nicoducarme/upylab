def appliquer(a,b,f):
    if type(f(a,b)) == float:
        return None
    else:
        return f(a,b)
