'''
Задача №49.

Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''

from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NameError(Exception):         # Объявляем исключение
    def __init__(self, txt):
        self.txt = txt


def GetInfo():
    isValidFirstName = False
    while not isValidFirstName:
        try:                                        # Выполняем проверку на исключения
            firstName = input('Введите имя')
            if len(firstName) < 2:
                raise NameError('Невалидное имя')   # Выбрасываем исключение
            else:
                isValidFirstName = True

        except NameError as err:                    # Отлавливаем исключение
            print(err)                              # Обработка исключения
            continue

    isValidLastName = False
    while not isValidLastName:
        try:
            lastName = input('Введите Фамилию')
            if len(lastName) < 2:
                raise NameError('Невалидная фамилия')
            else:
                isValidLastName = True

        except NameError as err:
            print(err)
            continue

    isValidPhone = False
    while not isValidPhone:
        try:
            phoneNumber = int(input('Введите номер'))
            if len(str(phoneNumber)) != 11:
                raise LenNumberError('Неверная длинна номера')
            else:
                isValidPhone = True

        except ValueError:
            print('Не валидный номер')
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [firstName, lastName, phoneNumber]


def CreateFile(fileName):
    # with open() - Менеджер контекста
    with open(fileName, 'w', encoding='utf-8') as data:
        fWriter = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        fWriter.writeheader()   # Записываем заголовок


def ReadFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as data:
        fReader = DictReader(data)
        return list(fReader)


def WriteFile(fileName, list1):
    res = ReadFile(fileName)    # создаём словарь (res) в который читаем содержимое файла

    for elem in res:                            # Выполняем проверку на совпадение
        if elem["Телефон"] == list1[2]:         # вводимого телефона с уже существующими
            print('Такой телефон уже есть')
            return                              # Полностью выходим из функции и начинаем
                                                # всё заново


    obj = {"Имя": list1[0], "Фамилия": list1[1], "Телефон": list1[2]}
    res.append(obj)                         # дополняем словарь-res
    with open(fileName, 'w', encoding='utf-8', newline='') as data:
        fWriter = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        fWriter.writeheader()               # Записываем заголовок
        fWriter.writerows(res)              # передаём в файл список со словарями


fileName = 'phone.csv'


def main():
    while True:
        command = input('Введите комманду: ')
        if command == 'q':                  # Выход из программы
            break

        elif command == 'w':                # Запись данных
            if not exists(fileName):        # Проверка наличия файла
                CreateFile(fileName)        # Если нет - создаём новый
            WriteFile(fileName, GetInfo())

        elif command == 'r':                # Чтение данных
            if not exists(fileName):        # Проверка наличия файла
                print('файл отсутствует')   # Если нет - возвращаемся в главное меню
                continue
            print(*ReadFile(fileName))


main()
