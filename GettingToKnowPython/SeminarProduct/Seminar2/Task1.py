import random

n = int(input("Введите число: "))
min = 20
max = 1

for _ in range(n):
    val = random.randint(1, 20)
    if val > max:
        max = val
    elif val < min:
        min = val

print(f"Макс арбуз - {max}, Мин арбуз - {min}")