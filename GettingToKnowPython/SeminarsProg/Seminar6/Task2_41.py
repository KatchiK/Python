"""
41. Дан список, состоящий из целых чисел.
Напишите программу, которая в данном списке определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
"""

import random
print(lst := [random.randint(0, 20) for i in range(10)])

count = 0
for i in range(1, len(lst) - 1):
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        count += 1

print(count)

print(len([lst[i] for i in range(1, len(lst) - 1) if lst[i] > lst[i - 1]
           and lst[i] > lst[i + 1]]))
