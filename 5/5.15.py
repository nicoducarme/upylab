def my_remove(lst, e):
    if isinstance(lst, list) == True:
        count = 0
        for c in lst:
            if c == e:
                lst.pop(count)

            else:
                count+=1
