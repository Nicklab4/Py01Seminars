""" Задача №67.
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('penguins.csv')

df.loc[df['bill_length_mm'] < 35, 'height_group'] = 'low'
df.loc[(df['bill_length_mm'] >= 35) & (df['bill_length_mm'] < 42), 'height_group'] = 'middle'
df.loc[df['bill_length_mm'] >= 42, 'height_group'] = 'high'

df.to_csv('penguins.csv')
