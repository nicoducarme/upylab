def my_insert(sorted_list, n):
    assert isinstance(n, int)
    sorted_list.append(n)
    sorted_list.sort()
    return None
