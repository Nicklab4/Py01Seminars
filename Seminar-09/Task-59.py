"""Задача №59.
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""

import pandas as pd

df = pd.read_csv('california_housing_test.csv')

print("Показать есть ли в файле пустые значения")
print(df.isnull().sum())

print("Показать median_house_value где median_income < 2")
print(df[df['median_income'] < 2]['median_house_value'])

print("Показать данные в первых 2 столбцах")
# Стандартный вывод при помощи жёстко заданных имён
# print(df[["longitude", "latitude"]])

# Вывод при помощи срезов
# Сперва задаются параметры вывода строк ":" - все строки
# Затем указываются параметры вывода столбцов ":2" - первые два столбца
print(df.iloc[:, :2])

print("Выбрать данные где housing_median_age < 20 и median_house_value > 70000")
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])
