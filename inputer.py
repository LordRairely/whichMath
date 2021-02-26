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
                    if len(line) - 1 != n:
                        print("Ты пытался меня обмануть\n" +
                              "введи строку заново")
                    else:
                        a.append(line)
                        break
            return a
        else:
            print("Введи нормально")

    except ValueError:
        print("Здесь такое не прокатит")


def file_input():
    try:
        n = 0
        a = []
        print("Формат ввода такой:\n" +
              "\t размерность матрицы\n" +
              "\t a11 a12 ... a1n b1\n" +
              "\t a21 a22 ... a2n b2\n" +
              "\t ... ... ... ...  ...\n" +
              "\t an1 an2 ... ann bn")
        path = input("Напиши путь к файлу:").strip()
        with open(path, 'r', encoding='utf-8') as file:
            file_to_lines = file.read().split("\n")
            n = int(file_to_lines[0])
            file_to_lines.pop(0)
            if 20 >= n > 1:
                for i in range(n):
                    a.append([float(el) for el in file_to_lines[i].split()])
                return a
            else:
                print("Проверь-ка ещё раз содержимое файла")
    except FileNotFoundError:
        print("Здесь " + path + " ничего не нашлось")
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
        print("Ну нормааально можно ввести")
    return a
