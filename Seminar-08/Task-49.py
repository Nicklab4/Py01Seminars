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


def GetInfo():
    firstName = 'Иван'
    lastName = 'Иванов'
    phoneNumber = '89531585239'
    return [firstName, lastName, phoneNumber]


def CreateFile(fileName):
    # Менеджер контекста
    with open(fileName, 'w', encoding='utf-8') as data:
        fWriter = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        fWriter.writeheader()  # Записываем заголовок


def ReadFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as data:
        fReader = DictReader(data)
        return list(fReader)


def WriteFile(fileName, list1):
    res = ReadFile(fileName)  # создаём словарь (res) в который читаем содержимое файла
    obj = {"Имя": list1[0], "Фамилия": list1[1], "Телефон": list1[2]}
    res.append(obj)  # дополняем словарь-res
    with open(fileName, 'w', encoding='utf-8', newline='') as data:
        fWriter = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        fWriter.writeheader()  # Записываем заголовок
        fWriter.writerows(res)  # передаём в файл список со словарями


fileName = 'phone.csv'


def main():
    while True:
        command = input('Введите комманду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(fileName):
                CreateFile(fileName)
            WriteFile(fileName, GetInfo())
        elif command == 'r':
            if not exists(fileName):
                print('файл отсутствует')
                continue
            print(*ReadFile(fileName))

main()