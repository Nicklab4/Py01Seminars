""" Задача №65.
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('penguins.csv')

# # sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g")
# sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g",
#                 hue="sex", size="island", style="island")
# plt.show()

# # Использовать PairGrid с типом графика на ваш выбор
# x_vars = ['body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
# y_vars = ['sex']
#
# pg = sns.PairGrid(df, x_vars=x_vars, y_vars=y_vars, hue='species')
# pg.map(sns.scatterplot)
#
# plt.show()

# # Изобразить Heatmap
# data = df.pivot_table(index='species', columns='island', values='body_mass_g')
# sns.heatmap(data)
# plt.xlabel(xlabel='остров', size=14)
# plt.ylabel(ylabel='Вид пингвина', size=14)
#
# plt.show()

sns.histplot(data=df, x='flipper_length_mm', hue='height_group')

plt.show()

