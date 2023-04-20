def qick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i>pivot]
    return qick_sort(less) + [pivot] + qick_sort(greater)


import random
lst = [random.randint(0, 20) for i in range(10)]
print(lst)
print(qick_sort(lst))