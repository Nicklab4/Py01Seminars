"""
Задача №57.
1. Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы

"""

import pandas as pd

df = pd.read_csv('california_housing_test.csv')
print("Количество строк и столбцов")
print(df.shape)
print("Типы данных столбцов")
print(df.dtypes)
print("Info")
print(df.info())
print("describe")
print(df.describe())