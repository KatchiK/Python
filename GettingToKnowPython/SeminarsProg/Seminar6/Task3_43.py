"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
"""

import random
print(lst := [random.randint(0, 5) for i in range(15)])

print(len([i for i in lst if lst.count(i) > 1])//2)

#sum(1 for i in range(n-1) for j in range(i+1, n) if lst[i] == lst[j]))

#print(sum(1 for i in range(n-1) for j in range(i+1, n)
#          if lst[i] == lst[j])))

print(len([i for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] == lst[j]]))