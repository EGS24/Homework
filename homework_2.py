def exercise_1():
    print("Занятие 1.")
    general = [1, 5, 3]
    side_1 = [1, 5, 1, 5]
    side_2 = [1, 3, 1, 5, 3, 3]
    general += side_1
    print("Кол-во цифр 5 при первом объединении:", general.count(5))
    general += side_2
    print("Кол-во цифр 3 при втором объединении:", general.count(3))
    print("Итоговый список:", general)


def exercise_2():
    print("Занятие 2.")
    first_class = list(range(160, 176, 2))
    second_class = list(range(162, 180, 3))
    general = sorted(first_class + second_class)
    print("Отсортированный список учеников:", general)


def exercise_3():
    print("Занятие 3.")
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
            ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]

    detail = input("Введите название детали:")
    count = 0
    price = 0
    for i in shop:
        if i[0] == detail:
            count += 1
            price += i[1]
    print("Название детали: {}\n"
          "Кол-во деталей — {}\n"
          "Общая стоимость — {}".format(detail, count, price))


def exercise_4():
    print("Занятие 4.")
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    print("Сейчас на вечеринке {} человек:{}".format(len(guests), guests))
    while (proposal := str(input("Гость пришёл или ушёл?"))) != "Пора спать":
        name = str(input("Имя гостя:"))
        if proposal == "пришёл" and len(guests) != 6:
            guests.append(name)
            print("Сейчас на вечеринке {} человек:{}".format(len(guests), guests))
        elif proposal == "пришёл" and len(guests) == 6:
            print(f"Прости,{name}, но мест нет")
            print("Сейчас на вечеринке {} человек:{}".format(len(guests), guests))
        elif proposal == "ушёл":
            guests.remove(name)
            print("Сейчас на вечеринке {} человек:{}".format(len(guests), guests))
    else:
        print("Вечеринка закончилась, все легли спать.")


def exercise_5():
    print("Занятие 5.")
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    count_songs = int(input("Сколько песен выбрать?"))
    count_time = 0
    name_songs = [songs[0] for songs in violator_songs]

    for i in range(count_songs):
        song_name = input(f"Название {i + 1}-й песни: ")
        song_index = name_songs.index(song_name)
        count_time += violator_songs[song_index][1]

    print(f"Общее время звучания песен: {round(count_time, 2)} минуты")


def exercise_6():
    print("Занятие 6.")
    list_numbers_1, list_numbers_2 = list(), list()
    for i in range(3):
        list_numbers_1.append(int(input(f"Введите {i + 1}-e число для первого списка:")))
    for i in range(7):
        list_numbers_2.append(int(input(f"Введите {i + 1}-e число для второго списка:")))
    print(f"Первый список:{list_numbers_1}\n"
          f"Второй список:{list_numbers_2}\n"
          f"Новый первый список с уникальными элементами:{list(set(list_numbers_1 + list_numbers_2))}")


def exercise_7():
    print("Занятие 7.")
    amount = 0
    list_of_skates, list_of_people = list(), list()
    for i in range(int(input("Кол-во коньков:"))):
        list_of_skates.append(int(input(f"Размер {i + 1}-й пары:")))
    for i in range(int(input("Кол-во людей:"))):
        list_of_people.append(int(input(f"Размер ноги {i + 1}-го человека:")))
    for i in list_of_people:
        if i in list_of_skates:
            list_of_skates.remove(i)
            amount += 1
    print("Наибольшее кол-во людей, которые могут взять ролики:", amount)


def exercise_8():
    print("Занятие 8.")
    people_count = int(input("Кол-во человек: "))
    number_in_rhyme = int(input("Какое число в считалке? "))
    number_people = [
        *range(1, 1 + people_count)]  # равноценно [i for i in range(1, 1 + people_count)] создается новый список
    point, shift = 0, 1
    while True:
        print("Текущий круг людей:", number_people)
        if len(number_people) < 2:
            print("Остался человек под номером", number_people[0])
            break
        print("Начало счёта с номера", number_people[point % len(number_people)])
        point += number_in_rhyme - shift
        shift += 1
        print("Выбывает человек под номером", number_people[point % len(number_people)])
        number_people.remove(number_people[point % len(number_people)])


def exercise_9():
    print("Занятие 9.")
    friends_count = int(input("Кол-во друзей: "))
    iou = int(input("Долговых расписок: "))
    friends = dict().fromkeys([*range(1, friends_count + 1)], 0)

    for i in range(iou):
        print(f"{i + 1}-я расписка")
        to_whom = int(input("Кому: "))
        from_whom = int(input("От кого: "))
        amount = int(input("Сколько: "))
        friends[to_whom] -= amount
        friends[from_whom] += amount

    print("Баланс друзей:")
    for friend, money in friends.items():
        print("{} : {}".format(friend, money))


def exercise_10():
    print("Занятие 10.")
    main_list = list()
    for i in range(int(input("Кол-во чисел: "))):
        main_list.append(int(input(f"Число: ")))
    secondary_list = main_list.copy()
    secondary_list.reverse()
    for i in range(len(main_list)):
        if secondary_list[i] != main_list[len(main_list) - 1]:
            secondary_list = secondary_list[i:]
            break
    print(
        "Последовательность: {} \n"
        "Нужно приписать чисел: {}\n"
        "Сами числа: {}".format(main_list, len(secondary_list), secondary_list)
    )


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
