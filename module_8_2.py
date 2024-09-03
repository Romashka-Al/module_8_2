def personal_sum(numb):
    res = 0
    incorrect_data = 0
    for el in numb:
        try:
            res += el
        except TypeError:
            incorrect_data += 1
    return res, incorrect_data


def calculate_average(numb):
    try:
        a, b = personal_sum(numb)
        return a / (len(numb) - b)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Первый результат: {calculate_average("5, qwerty, 6, UwU")}')
print(f'Второй результат: {calculate_average([52, "Йоу", "Я календарь, переверну, и снова", 3, "ье сентября", 1000, 7, "Le-le-let me"])}')
print(f'Третий результат: {calculate_average([100, 4, 42, 33, 15, 8, 9, 10, 2, 50, 12])}')
print(f'Четвёртый результат: {calculate_average(777)}')
