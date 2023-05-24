import random
lst = [random.randint(0, 20) for i in range(10)]
print(lst)
res = list()

for i in lst:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

res = select(int, lst)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res)

res = list(select(lambda x: (x, x**2), res))
print(res)