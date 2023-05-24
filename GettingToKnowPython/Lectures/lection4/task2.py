def amount(x, y):
    return x+y

def product(x, y):
    return x*y

def calc(op,a, b):
    print (op(a, b))

n = 5
m = 6
calc(amount, n, m)
calc(product, n, m)

calc(lambda a,b: a+b, n,m)#Равносильна функции amount

calc(lambda a,b: a*b, n,m)#Равносильна функции product

