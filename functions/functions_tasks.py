# Написати функцію, яка приймає рядок і повертає кількість голосних букв у цьому рядку.

def pidrahunok(a):
    holosni = 'eyuioaEYUIOA'
    string = [i for i in a if i in holosni]
    return len(string)


# print(pidrahunok('Hello WOrld'))

# Написати функцію, яка приймає два числа та повертає їх суму.

def dodavannya(x,y):
    return x + y

# print(dodavannya(3,7))

# Написати функцію, яка приймає список чисел і повертає найбільше число в цьому списку.
# def printMax(a):
#     return max(a)

# print(printMax([1,2,35555,4,5,6,7,8]))

# Написати функцію, яка приймає список і повертає список, який містить тільки унікальні елементи вихідного списку.

def uniq(a):
    return list(set(a))

# print(uniq([1,1,2,2,3,3,3,4,4,4,4,6,6,7,6,76,]))

# Написати функцію, яка приймає список чисел та повертає суму квадратів цих чисел.

def squares(a):
    return sum(item ** 2 for item in a)

# print(squares([1,2,3]))

# Написати функцію, яка приймає список і повертає список, 
# який складається з елементів вхідного списку у зворотному порядку.

def backwards(a):
    return sorted(a, reverse= True) # a[::-1]

# print(backwards([1,7,4,65,7]))

# Написати функцію, яка приймає список і повертає кількість 
# елементів у цьому списку, що більші за середнє значення списку.

def above_avg(lst):
    avg = sum(lst) / len(lst)
    print(avg)
    suma = 0  # return sum(1 for i in lst if i > avg)
    for i in lst:
        if i > avg:
            suma +=1
    return suma

# print(above_avg([1,2,3,4,5,6,7,8,9]))

# Написати функцію, яка приймає список рядків та повертає новий список, 
# який містить тільки ті рядки, що складаються тільки з літер або цифр.

def iiii(lst):
    return [i for i in lst if i.isalstr()]


print(iiii(['erer12123', 'sdfsf', '213213', 'sdfsdf!@!#@#', '232323^$%$']))