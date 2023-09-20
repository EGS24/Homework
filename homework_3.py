from datetime import datetime
from math import gcd, lcm
import datetime


def exercise_1():
    numbers = [int(input("Введи число в список:")) for i in range(int(input("Введите длину списка:")))]
    print("НОД чисел: {}, НОК чисел: {} ---> Cписка: {}".format(gcd(*numbers), lcm(*numbers), numbers))


def exercise_2():
    text = []
    for element_text in range(int(input("Введите количество предложений:"))):
        text.append(input("Введите предложение:"))
    count = len([i for i in text if any(map(str.isdigit, i))])
    print(count)


def exercise_3():
    text = input("Введите строку:")
    symbol = input("Введите символ:")
    for i in range(3):
        if i == 0 or i == 2:
            print(symbol * (len(text) + 2))
        else:
            print(symbol + text + symbol)


def exercise_4():
    text = input("Введите предложение:").lower()
    uniq = set(text)
    print(text)
    print("Количество вхождений символа в строку:")
    for i in uniq:
        a = text.count(i)
        print("{} : {}".format(i, a))


def exercise_5():  # Шифр Цезаря
    def coder():
        text = str(input("Введите строку на русском языке:"))
        step = int(input("Введите шаг кодировки:"))
        text_coder = ''
        text_de_coder = ''

        def coder_func(c):
            count = 0
            char = ''
            if 'а' <= c <= 'я' or 'А' <= c <= 'Я':
                for a in c:
                    count = ord(a)
                    for b in range(step):
                        if count == 1071 or count == 1103:
                            count -= 31
                        else:
                            count += 1
                char += chr(count)
            else:
                return c
            return char

        def de_coder(c):
            count = 0
            char = ''
            if 'а' <= c <= 'я' or 'А' <= c <= 'Я':
                for a in c:
                    count = ord(a)
                    for b in range(step):
                        if count == 1040 or count == 1072:
                            count += 31
                        else:
                            count -= 1
                char += chr(count)
            else:
                return c
            return char

        for i in text:
            text_coder += coder_func(i)
        print(text_coder)

        for i in text_coder:
            text_de_coder += de_coder(i)
        print(text_de_coder)

    def main_5():
        coder()

    main_5()


def exercise_6():
    def func(*nums):
        negative, positive = list(), list()
        for i in sorted(nums):
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        return sorted(negative, reverse=True), positive

    return print(tuple(func(1, 3, 2, 3, 5, -5, -2, -4, -8, -2, -1, -1, 0, 4, 2, 1, 4, 7)))


def exercise_7():
    def is_palindrome(a: str):
        flag = False
        for i in range(0, (len(a) // 2)):
            if a[i] == a[len(a) - i - 1]:
                flag = True
            else:
                return False
        return flag

    if is_palindrome(text := str(input("Введите строку:"))):
        print('Строка "{}" является палиндромом.'.format(text))
    else:
        print('Строка "{}" не является палиндромом.'.format(text))


def exercise_8():
    # n = int(input("Введите число для поиска:"))
    # start, end, count = 0, 100, 0
    # while 1:
    #     count += 1
    #     print("Твое число равно, меньше или больше, чем число N?")
    #     number_computer = (start + end) // 2
    #     if n == number_computer:
    #         print("Вы нашли число {} за {} попыток.".format(n, count))
    #         break
    #     elif n < number_computer:
    #         print("Мое число {}, меньше, чем число N:{}".format(n, number_computer))
    #         end = number_computer - 1
    #     elif n > number_computer:
    #         print("Мое число {}, больше, чем число N:{}".format(n, number_computer))
    #         start = number_computer + 1
    # --------------------------------------------------------------------------------------------------2 вида
    start, end, count = 0, 100, 0
    while 1:
        count += 1
        middle = (start + end) // 2
        result = int(input(f"Твое число равно 1, больше 2 или меньше 3, чем число {middle}? ---> "))
        if result == 1:
            return print(f"Число найдено за {count} попыток!")
        elif result == 2:
            start = middle + 1
        elif result == 3:
            end = middle - 1


def exercise_9():
    number = int(input("Введите число:"))
    system_coder = int(input("Введите систему счисления в которую переводить число:"))
    system_de_coder = int(input("Введите систему счисления из которой переводить число:"))

    def coder(num: int, sys: int):  # перевод из десятичной в любую систему счисления
        if sys < 2 or sys > 16:
            return print("Вы ввели неправильную систему счисления")
        result = ''
        while num != 0:
            c = num % sys
            if c < 10:
                result = str(c) + result
            else:
                result = chr(ord('A') + c - 10) + result
            num //= sys
        return result

    def de_coder(num: str, sys_de_coder: int):  # перевод из любой в десятичную систему счисления
        if sys_de_coder < 2 or sys_de_coder > 16:
            return print("Вы ввели неправильную систему счисления")
        pow_step = 1
        ans = 0
        for i in num[::-1]:
            if i < 'A':
                ans += int(i) * pow_step
            else:
                ans += (ord(i) - ord('A') + 10) * pow_step
            pow_step *= sys_de_coder
        return ans

    def main_9():
        result_coder = coder(number, system_coder)
        print("Результат перевода:", result_coder)
        result_de_coder = de_coder(str(result_coder), system_de_coder)
        print("Результат обратного перевода:", result_de_coder)

    main_9()


def exercise_10():
    day = int(input("Введите день:"))
    month = int(input("Введите месяц:"))
    year = int(input("Введите год:"))

    def is_magic_date(number_day: int, number_month: int, number_year: int):
        if number_day < 1 or number_day > 31 or number_month < 1 or number_month > 12 or number_year == 0:
            return "Неправильно введены данные"
        return number_day * number_month == number_year % 100

    def is_magic_century():
        amount = 0
        for y in range(1900, 2000):
            for m in range(1, 13):
                for d in range(1, 32):
                    try:
                        date = datetime.date(y, m, d)
                    except ValueError:  # чтобы шел цикл дальше, ибо range 31, а дней в месяце может быть меньше
                        continue
                    if is_magic_date(date.day, date.month, date.year):
                        amount += 1
                        print(f"{amount} - ", date.strftime("%d.%m.%Y"))
        print(f"Общее количество магических дат в 20 веке: {amount}")

    def main_10():
        if is_magic_date(day, month, year):
            print("Дата является магической.")
        else:
            print("Дата не является магической.")
        is_magic_century()

    main_10()


def main():
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()


main()
