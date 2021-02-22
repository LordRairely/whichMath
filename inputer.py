import random


def console_input():
    a = []  # массивчик для матрички
    try:
        n = int(input("Размерность матрицы "
                      "(вместитесь в диапазон от 1 до 20 включительно):").strip())
        if 20 >= n > 1:
            print("Вводите матричку вооот так:\n" +
                  " ai1 ai2 ... aij bi ")  # ведите матричку
            for i in range(n):
                while True:  # зочем
                    line = (input(str(i + 1) + ". ").split())
                    if len(line) - 1 != n:  # переписать ввод без палки
                        print("Ты пытался меня обмануть\n" +
                              "введи строку заново")
                    else:
                        a.append(line)  # append() - добавляет элемент в конец списка
                        break
            return a
        else:
            print("Введи нормально")

    except ValueError:
        print("Бля опять хуйню ввел")


def file_input():
    try:
        n = 0
        a = []
        print("Бля формат ввода такой:\n" +
              "\t размерность матрицы\n" +
              "\t a11 a12 ... a1n b1\n" +
              "\t a21 a22 ... a2n b2\n" +
              "\t ... ... ... ...  ...\n" +
              "\t an1 an2 ... ann bn")
        path = input("Бля напиши путь:").strip()
        with open(path, 'r', encoding='utf-8') as file:
            file_to_lines = file.read().split("\n")
            n = int(file_to_lines[0])
            if 20 >= n > 1:
                for i in range(n):
                    a.append([float(el) for el in file_to_lines[i].split()])
                return a
            else:
                print("Бля файл говна")
    except FileNotFoundError:
        print("File " + path + " don't exist.")
        return
    except UnboundLocalError:
        return


def random_system():
    a = []
    try:
        n = int(input("Размерность матрицы "
                      "(вместитесь в диапазон от 1 до 20 включительно):").strip())
        if 20 >= n > 1:
            for i in range(n):
                line = []
                for j in range(n):
                    line.append(random.random() * 200 - 100)
                    line.append(random.random() * 200 - 100)
                a.append(line)
        print(a)
    except ValueError:
        print("Incorrect input.")
    return a
