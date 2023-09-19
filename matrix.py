# открываем файлы с матрицами
with open("matrix1.txt") as f1, open("matrix2.txt") as f2:
    # считываем матрицы из файлов
    matrix1 = [[int(num) for num in line.split()] for line in f1]
    matrix2 = [[int(num) for num in line.split()] for line in f2]

# определяем количество строк и столбцов для каждой матрицы
rows1 = len(matrix1)
cols1 = len(matrix1[0])
rows2 = len(matrix2)
cols2 = len(matrix2[0])


if cols1 != rows2:
    print("Невозможно перемножить матрицы")
else:
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # выполняем умножение матриц
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    with open("result.txt", "w") as f:
        for row in result:
            f.write(" ".join(str(num) for num in row) + "\n")

    print("Успешно записан результат в файл 'result.txt'")

"""
Пример содержимого файлов matrix1.txt и matrix2.txt (записанных построчно):


1 2 1 2 0 3 2 4
2 3 5 1 3 7 5 2
1 3 5 8 2 7 0 0
4 5 6 7 2 1 3 5



4 5 5 5
1 2 3 3
0 0 0 0
0 0 1 1
1 1 2 2
3 2 1 1
-2 -3 -1 0
1 2 3 1


В файле result.txt будет содержаться результат умножения матриц, например:


10 13 12 12
33 40 37 20
45 56 48 38
64 78 71 47"""
