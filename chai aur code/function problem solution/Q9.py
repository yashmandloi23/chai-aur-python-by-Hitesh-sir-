def even_num(limit):
    li = []
    for i in range(2, limit+1, 2):
        li.append(i)
    return li
print(even_num(5))