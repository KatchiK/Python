"""Задача 14: Требуется вывести все целые степени двойки 3
(т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""
stop = False
num = 50
prod = 0
i = 0
while stop == False:
    prod = 2**i
    if num <= prod:
        stop = True
    else:
        print(prod)
    i += 1
