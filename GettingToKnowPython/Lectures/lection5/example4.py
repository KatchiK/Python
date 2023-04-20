def fbn(n):
    if n in [1,2]:
        return 1
    return fbn(n-1) + fbn(n-2)

lst = []
for i in range (1,10):
    lst.append(fbn(i))
print(*lst)