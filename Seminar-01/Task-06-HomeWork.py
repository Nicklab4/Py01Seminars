'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и
выводит на экран yes или no.

Пример:
n = 385916 -> yes
n = 123456 -> no
'''

n = 123456

# Введите ваше решение ниже

temp1 = 0
temp2 = 0
OneHalf = str(n)[:3]
TwoHalf = str(n)[3:]

for i in OneHalf:
    temp1 += int(i)

for j in TwoHalf:
    temp2 += int(j)

if temp1 == temp2:
    print('yes')
else:
    print('no')