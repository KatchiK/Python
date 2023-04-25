"""
39. Даны два списка чисел. 
Требуется вывести те элементы первого списка 
(в том порядке, в каком они идут в первом списке), которых нет во втором массиве.
"""
# n = int(input())

import random
lst1 = [random.randint(0, 10) for i in range(10)]
print(lst1)
lst2 = [random.randint(0, 10) for i in range(10)]
print(lst2)

result = [x for x in lst1 if x not in lst2]

print(f"Вариант 1: {result}")

for i in lst1:
    if i not in lst2:
        print(f'Во втором списке нет числа {i}')
