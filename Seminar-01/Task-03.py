'''
Задача №3.

В некоторой школе решили набрать три новых математических класса и оборудовать
кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

sum = 0

# Первый вариант решения
if a % 2:
    sum = sum + a//2 + 1
else:
    sum = sum + a//2
#print(sum)
if b % 2:
    sum = sum + b//2 + 1
else:
    sum = sum + b//2
#print(sum)
if c % 2:
    sum = sum + c//2 + 1
else:
    sum = sum + c//2

print(sum)

# Второй вариант решения
sum = 0

for i in a, b, c:
    if i % 2:
        sum = sum + i // 2 + 1
    else:
        sum = sum + i // 2

print(sum)