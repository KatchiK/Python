"""Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
*Пример:*
2 2
    4 
"""
num_a = int(input("Введите число a: "))
num_b = int(input("Введите число b: "))

def amount(a, b):
    if b < 1:
        return a
    return amount(a+1, b-1)

print(amount(num_a, num_b))
#потом коммент удалить