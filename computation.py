def computate(a):
    try:
        print("\nТвоя матрица:\n")
        print_system()

        make_triangle(a)
        print("\nTriangle system:\n")
        print_system(a)
        determinate(a)
        x_calculation(a)
        print_x()
        get_residuals()
    except ZeroDivisionError:
        print("")
        return
    except ArithmeticError:
        print("")
        return

    def __check_diagonal(self, i):
        j = i
        while j < self.n:
            if self.system[j][i] != 0 and self.system[i][j] != 0:
                swap = self.system[j]
                self.system[j] = self.system[i]
                self.system[i] = swap
                self.swap += 1
                return
            j += 1
        print("No solutions")
        return ArithmeticError

def determinate(a):
    i = 0
    det = 1
    while i < n:
        det *= system[i][i]
        i += 1
    if swap % 2 == 1:
        det *= -1
    print("\nDeterminant: " + str(det))
    if det == 0:
        print("This is degenerate system, no solution.")
        return ArithmeticError

    def __make_triangle(self):
        try:
            i = 0
            while i < self.n:
                if self.system[i][i] == 0:
                    self.__check_diagonal(i)
                m = i
                while m < self.n - 1:
                    a = -(self.system[m + 1][i] / self.system[i][i])
                    j = i
                    while j < self.n:
                        self.system[m + 1][j] += a * self.system[i][j]
                        j += 1
                    self.system[m + 1][-1] += a * self.system[i][-1]
                    m += 1
                k = 0
                line_sum = 0
                while k < self.n:
                    line_sum += self.system[i][k]
                    k += 1
                if line_sum == 0:
                    print("This system is incompatible, no solutions")
                    return ArithmeticError
                i += 1
        except ValueError:
            print("Incorrect working data.")
            return