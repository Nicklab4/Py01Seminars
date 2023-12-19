"""Задача №61.
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value
"""

import pandas as pd

df = pd.read_csv('california_housing_test.csv')

print('Максимальное и минимальное значение median_house_value')
print(df['median_house_value'].max(), df['median_house_value'].min())

print('Показать максимальное median_house_value, где median_income = 3.1250')
print(df[df['median_income'] == 3.1250]['median_house_value'].max())

print('Узнать какая максимальная population в зоне \n'
      'минимального значения median_house_value')
print(df[df['median_house_value'] == df['median_house_value'].min()]['population'].max())
