"""
Задача №49.

Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


# Объявляем исключение
class NameError(Exception):  
    def __init__(self, txt):
        self.txt = txt


def get_info():
    first_name = last_name = phone_number = ''

    is_valid_first_name = False
    while not is_valid_first_name:
        # Выполняем проверку на исключения
        try:  
            first_name = input('Введите имя')
            if len(first_name) < 2:
                # Выбрасываем исключение
                raise NameError('Невалидное имя')  
            else:
                is_valid_first_name = True

        # Отлавливаем исключение
        except NameError as err:
            # Обработка исключения
            print(err)  
            continue

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input('Введите Фамилию')
            if len(last_name) < 2:
                raise NameError('Невалидная фамилия')
            else:
                is_valid_last_name = True

        except NameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер'))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длинна номера')
            else:
                is_valid_phone = True

        except ValueError:
            print('Не валидный номер')
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with open() - Менеджер контекста
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        # Записываем заголовок
        f_writer.writeheader()  


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, list1):
    # создаём словарь (res) в который читаем содержимое файла
    res = read_file(file_name)

    # Выполняем проверку на совпадение
    for elem in res:
        # вводимого телефона с уже существующими
        if elem["Телефон"] == list1[2]:  
            print('Такой телефон уже есть')
            # Полностью выходим из функции и начинаем всё заново
            return

    obj = {"Имя": list1[0], "Фамилия": list1[1], "Телефон": list1[2]}
    # дополняем словарь-res
    res.append(obj)  
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        # Записываем заголовок
        f_writer.writeheader()
        # передаём в файл список со словарями
        f_writer.writerows(res)  


def copy_file(file_name, number_row):
    # Читаем файл в res
    res = read_file(file_name)
    # проверяем, есть ли такая строка?
    if number_row > len(res):  
        print('Нет такой строки в файле')
        return
    # print(res)
    temp = list()
    # в переменную temp - вырезаем искомое значение
    temp.append(res.pop(number_row - 1))  
    # print(temp)

    # Записываем изменения в первый файл
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        # Записываем заголовок
        f_writer.writeheader()
        # передаём в файл список со словарями
        f_writer.writerows(res)  

    # Записываем второй файл
    with open("Newfile_name.csv", 'w', encoding='utf-8', newline='') as data2:
        f_writer = DictWriter(data2, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        # Записываем заголовок
        f_writer.writeheader()
        # передаём в файл список со словарями
        f_writer.writerows(temp)  


def main():
    file_name = 'phone.csv'

    while True:
        command = input('Введите команду: ')
        # Выход из программы
        if command == 'q':  
            break

        # Запись данных
        elif command == 'w':
            # Проверка наличия файла
            if not exists(file_name):
                # Если нет - создаём новый
                create_file(file_name)  
            write_file(file_name, get_info())

        # Чтение данных
        elif command == 'r':
            # Проверка наличия файла
            if not exists(file_name):
                # Если нет - возвращаемся в главное меню
                print('файл отсутствует')  
                continue
            print(*read_file(file_name))

        # Копирование данных
        elif command == 'c':
            # Проверка наличия файла
            if not exists(file_name):
                # Если нет - возвращаемся в главное меню
                print('файл отсутствует')  
                continue
            number_row = int(input('Введите номер строки для копирования: '))
            copy_file(file_name, number_row)


main()
