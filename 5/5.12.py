def my_insert(sorted_list, n):
    if type(n) == int:
        sorted_list.append(n)
        sorted_list = sorted(sorted_list, reverse=False)
        return sorted_list
