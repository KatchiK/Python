"""Задача 8: 
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

chek = False

while chek == False: # Проверка введенного выражения
    
    try:
        m = int(input("Введите количество долек шоколадки по длине: "))
    except ValueError:
        print("Количество измеряется в натуральных числах")
    else:
        if int(m) < 0:
            print("Количество не может быть отрицательным. Попробуйте ещё раз.")
            chek = False
        else:
            chek = True

chek = False

while chek == False: # Проверка введенного выражения
    
    try:
        n = int(input("Введите количество долек шоколадки по ширине: "))
    except ValueError:
        print("Количество измеряется в натуральных числах")
    else:
        if int(n) < 0:
            print("Количество не может быть отрицательным. Попробуйте ещё раз.")
            chek = False
        else:
            chek = True

chek = False
while chek == False: # Проверка введенного выражения
    
    try:
        k = int(input("Введите интересующее количество долек шоколадки: "))
    except ValueError:
        print("Количество измеряется в натуральных числах")
    else:
        if int(k) < 0:
            print("Количество не может быть отрицательным. Попробуйте ещё раз.")
            chek = False
        else:
            chek = True

print(m,n,k)

if (k % n == 0 or k % m == 0) and (k <= n * (m - 1) or k <= m * (n - 1)):
    print(f"{k} дольки(ек) можно отломить от шоколадки размером {m}х{n} долек")
else:
    print(f"{k} дольки(ек) нельзя отломить от шоколадки размером {m}х{n} долек")

