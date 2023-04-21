"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""

num_a = int(input())
num_b = int(input())

def exponentiation(a, b):
    c = 0
    if b == 1:
        return a
    a = a*a
    exponentiation(a, b-1)

print(exponentiation(num_a, num_b))


