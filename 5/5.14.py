def my_count(lst, e):
    count = 0
    if isinstance(lst, list) == True:
        for c in lst:
            if c == e:
                count += 1
    return count
