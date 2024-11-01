# функция
def get_matrix(n = 3, m = 2, value = 10):
    matrix = []
    for i in range(n):
        list = []
        matrix.append(list)
        for j in range(m):
             list.append(value)
    return matrix
print(get_matrix())


