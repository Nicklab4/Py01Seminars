"""Задача 44:
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
"""
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Вывод 10 строк для наглядности и контроля результата
# и сохранение сгенерированных данных в csv файл
print(data.head(n=10))
data.to_csv('First_List.csv')

# Добавление столбца robots - заполненного нулями
data.loc[:, 'robots'] = '0'
# Производим выборку роботов и заносим результат в robots
data.loc[data['whoAmI'] == 'robot', 'robots'] = '1'

# Добавление столбца humans - заполненного нулями
data.loc[:, 'humans'] = '0'
# Производим выборку людей и заносим результат в humans
data.loc[data['whoAmI'] == 'human', 'humans'] = '1'

# Удаляем колонку с первоначальными значениями и сохраняем
# значения в новый ДатаФрейм - data2
data2 = data.drop(columns=['whoAmI'])

# Вывод 10 строк для наглядности и контроля результата
# и сохранение сгенерированных данных в csv файл
print(data2.head(n=10))
data2.to_csv('OneHot.csv')
