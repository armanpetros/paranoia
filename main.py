entered_name = ""  # Инициализация переменной для введенного имени
first_number = 0  # Инициализация переменной для первого числа
second_number = 0  # Инициализация переменной для второго числа
third_number = 0  # Инициализация переменной для третьего числа

def main():

    # Определение функции для ввода имени
    def enter_name():
        global entered_name
        name = " ".join(str(input("Enter your name: ")).split()).title()
        entered_name = name
        valid_name()  # вызов функции валидации имени

    # Определение функции для валидации введенного имени
    def valid_name():
        # Проверка, что длина имени не более 20 символов
        if len(entered_name) > 20:
            print("Your name length can't exceed 20 symbols")
            main()

        # Проверка, что имя состоит из 1 или 2 слов
        words_in_name = entered_name.split()
        words_count = len(words_in_name)
        if words_count > 2 or entered_name == "":
            print("Name should contain from one to two words!")
            main()

        # Проверка, что слова в имени состоят только из букв
        for word in entered_name.split():
            if word.isalpha():
                continue
            print("Name should contain only letters!")
            main()

        # Определение условия для остановки программы
        if entered_name == "Stop":
            print("You requested to Stop!")
            exit()
        else:
            print(f"{entered_name}, hi!")  # вывод приветствия

    enter_name()  # вызов функции ввода имени

    # Определение функции для валидации введенного значения
    def first_number_validation():
        global first_number
        while True:
            try:
                number = int(input("Please enter first number: "))
            except ValueError:
                number = None
            if number is None:
                print("Please enter number only")
                continue
            elif number <= 0:
                print("Number should be greater than 0")
                continue
            else:
                break
        first_number = int(f"{number}" * 3)

    first_number_validation()  # Вызов переменной для валидации первого числа
    print(first_number)  # Вывод результата


    # Определение функции для валидации введенного значения
    def second_number_validation():
        global second_number
        while True:
            try:
                number = int(input("Please enter second number: "))
            except ValueError:
                number = None
            if number is None:
                print("Please enter number only")
                continue
            elif number <= 0:
                print("Number should be greater than 0")
                continue
            else:
                break
        second_number = int(f"{number}" * 3)

    second_number_validation()  # Вызов переменной для валидации второго числа
    print(second_number)  # Вывод результата

    # Определение функции для валидации введенного значения
    def third_number_validation():
        global third_number
        while True:
            try:
                number = float(input("Please enter third number: "))
            except ValueError:
                number = None
            if number is None:
                print("Please enter number only")
                continue
            elif number <= 0:
                print("Number should be greater than 0")
                continue
            else:
                break
        third_number = float(f"{number}")

    third_number_validation()  # Вызов переменной для валидации третьего числа
    print(third_number)  # Вывод результата

    S = (first_number + second_number) / third_number  # Переменная для выполнения математической операции с введенными данными
    print(S)  # Вывод результата
    main() # перезапуск

if __name__ == '__main__':
    main()
    