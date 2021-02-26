import copy


def print_matrix(a):
    for i in range(len(a)):
        for k in range(len(a) + 1):
            print(a[i][k], end="\t")
        print()


def computate(a):
    try:
        triangle_matrix, swaps = make_triangle(a)

        print("А вот и треугольная матрица")
        print_matrix(triangle_matrix)
        print()
        print("Держи детерминант")
        print(get_determinate(triangle_matrix, swaps))
        print()
        x = get_variables(triangle_matrix)
        print("Держи вектор неизвестных")
        print(x)
        print()
        print("Держи вектор невязок")
        print(get_residuals(a, x))

    except ZeroDivisionError:
        print("Ой йой на 0 делим...")
        return
    except ArithmeticError:
        print("Ашипочка")
        return


def get_variables(matrix):
    a = copy.deepcopy(matrix)
    n = len(a)
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += a[i][j] * x[j]
        x[i] = (a[i][-1] - s) / a[i][i]
    return x


def get_residuals(a, x):
    residuals = []
    for i in range(len(a)):
        s = 0
        for k in range(len(a)):
            s += a[i][k] * x[k]
        residuals.append(a[i][-1] - s)
    return residuals


def swap_lines(a, i):
    for k in range(i + 1, len(a)):
        if a[k][i] != 0:
            a[i], a[k] = a[k], a[i]
            return a
    print("Сори, решений нет")
    return ArithmeticError


def get_determinate(a, swaps):
    det = 1
    for i in range(len(a)):
        det *= a[i][i]
    det *= (-1) ** swaps
    return det


def make_triangle(matrix):
    try:
        a = copy.deepcopy(matrix)
        n = len(a)
        swaps = 0
        for i in range(n - 1):
            if a[i][i] == 0:
                a = swap_lines(a, i)
                swaps += 1
            for k in range(i + 1, n):
                c = a[k][i] / a[i][i]
                a[k][i] = 0
                for j in range(i + 1, n):
                    a[k][j] -= c * a[i][j]
                a[k][-1] -= c * a[i][-1]

        return a, swaps
    except ValueError:
        print("Ашипочка")
