def func():
    print('Hello world!')

# func() # виклик функції

def calc(x,y):
    print(x + y)

# calc(4, 7)

def aaa(x, y):
    print(f'{x} & {y}')

# aaa('Hello', True)


def triangle():
    for i in range(1,13):
        print('*' * i)

# triangle()


def printMax(a,b):
    if a > b:
        print(f'{a} - the biggest')
    elif a < b:
        print(f'{b} - the biggest')
    else:
        print('equal')

# printMax(2,3)
# printMax(89,7)
# printMax(8,8)


def exmpl(x,y):
    return x + y

a = exmpl(4,5)
# print(a)


def suma(x,y):
    return x + y

def diff(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y


def calculator(num1, num2, diya):
    if diya not in ['+', '-', '*', '/']:
        print('wrong action')
    else:
        if diya == '+':
            result = suma(num1, num2)
        elif diya == '-':
            result = diff(num1, num2)
        elif diya == '*':
            result = mult(num1, num2)
        else:
            result = div(num1, num2)

        print(f'{num1} {diya} {num2} = {result}')

# x, y, diy= input().split()

# calculator(int(x), int(y), diy)



x = 50

# def bbb():
#     x = 2
#     print(f'це Х з функції і його значення = {x}')

# bbb()
# print(f'{x} з-за меж функції')

def glob():
    global x
    print(f'x = {x}')
    x = 2
    print(f'міняємо глобальне Х на {x}')

# glob()
# print(f'x = {x}. а початкове було 50')



def fun(a ,b = 5,c = 10):
    print(f'a = {a}, b = {b}, c = {c}')

# fun(2,9)
# fun(7, c = 23)
# fun(1)
# fun(c = 0, a = 34)

def ogo(*a, **b):
    for i in a:
        print(i)
    for j,k in b.items():
        print(j, k)

# ogo(1,2,3,4,'hello', name = 'Jack', age = 25)






