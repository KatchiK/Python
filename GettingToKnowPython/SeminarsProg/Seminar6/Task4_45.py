"""
Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 10000. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
"""

#import math

k = int(input("Введите число k: "))

# Создаем кэш для хранения сумм делителей чисел
divisor_sums = [0] * (k+1)
for i in range(1, k+1):
    for j in range(i*2, k+1, i):
        divisor_sums[j] += i

# Используем кэш для проверки дружественности чисел
for i in range(1, k+1):
    for j in range(i+1, k+1):
        if divisor_sums[i] == j and divisor_sums[j] == i:
            print(i, j)

