from inputer import console_input, file_input, random_system
from computation import computate

import sys

print("Доброго времени с уток!")

while True:
    matrix = []
    try:
        print("Как будем поступать с матрицей:\n" +
              "\t1. Ввести самостоятельно\n" +
              "\t2. Прочитать из файла\n" +
              "\t3. Сгенерировать\n" +
              "\t4. Выйти в окно")
        answer = input().strip()
        if answer == "1":
            matrix = console_input()
        elif answer == "2":
            matrix = file_input()
        elif answer == "3":
            matrix = random_system()
        elif answer == "4":
            sys.exit(0)  # чем отличается от брейка?
        else:
            print("Нормально со мной разговаривай")
            continue
        computate(matrix)
    except KeyboardInterrupt:  # че
        print("Всем спасибо, я всё...")
