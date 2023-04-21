"""Задача №35. Напишите функцию, которая принимает одно число и проверяет, 
является ли оно простым.
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

number = int(input("Введите число: "))

def prime_num(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
    return True

print(prime_num(number))
                