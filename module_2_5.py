def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
value = (input(f'Задайте значение матрицы: '))

matrix = get_matrix(n, m, value)

if n <= 0:
    print('Не верное задано количество строк')
elif m <= 0:
    print('Не верно задано количество столбцов')


for i in matrix:
    print(*i)



