"""
Задача 40: Дан файл california_housing_train.csv.
Определить среднюю стоимость дома, где количество людей от 0 до 500 (population)
и сохранить ее в переменную avg.
"""

import pandas as pd

df = pd.read_csv('california_housing_train.csv')

avg = df[(df['population'] >= 0) & (df['population'] < 500)]['medianHouseValue'].mean()

print(avg)
