def my_pow(max,b):
    pow_list = []
    if type(max) == int and type(b) == float:
        for i in range(max):
            pow_list.append(b**i)
        return pow_list
