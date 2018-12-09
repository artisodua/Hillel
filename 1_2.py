def even_num(x):
    ar = []
    for i in range(0, x):
        if i % 2 == 0:
            ar.append(i)
    return ar

value = int(100)
print(even_num(value))