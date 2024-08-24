# Створіть словник, який містить (ключ — ім’я студента. Значення — список із балами). Попросіть користувача ввести ім’я студента.
#  Порахувати середній бал студента, ім’я якого ввів користувач. 

students = {
    'Micah': [8,5,7,9,6,3],
    'Tanya': [3,5,7,3,2,8],
}

std = input('Enter name: ').capitalize()


if std in students:
    average = sum(students[std]) / len(students[std])
    print(f'{std} = {average:.2}')
else:
    print('takoho studenta nema')

# Створіть словник, який містить (ключ — ім’я студента. Значення — список із балами).
#  Напишіть програму, яка порахує середній бал усіх учнів та виведе його на екран.


for stud in students:
    avg = sum(students[stud]) / len(students[stud])
    print(f'{stud} = {avg:.2}')

for name, grade in students.items():
    avg = sum(grade) / len(grade)
    print(f'{name} = {avg:.2}')

# Створіть словник, який містить (ключ — назва книги. Значення — кількість сторінок у ній). 
# Напишіть програму, яка виводить на екран книгу з найбільшою кількістю сторінок. 
# Вивести на екран книгу з найменшою кількістю сторінок. Порахувати середнє значення сторінок у всіх книгах.

books = {
    'HP': 1500,
    'LOTR': 2000,
    'SW': 750,
}

max_p = max(books.values())
print(max_p)

min_p = min(books.values())
print(min_p)

avg = sum(books.values()) / len(books.values())
print(f'{avg:.2f}')


# Створіть словник, який містить дані про ціни на різні товари у різних магазинах.
#  Ключами в цьому словнику будуть назви товарів, а значеннями — словники з
#  назвами магазинів та цінами на ці товари у цих магазинах

products = {
    'chips': {
        'ATB': 64.50,
        'SILPO': 67.40,
        'SIM23': 60,
    },
    'cola': {
        'ATB': 50.50,
        'SILPO': 47.40,
        'SIM23': 92.99,
    },
    'mivina': {
        'ATB': 17.50,
        'SILPO': 21.40,
        'SIM23': 22.99,
    },
}

tovar = input('Sho treba?: ')

if tovar in products:
    stores = products[tovar]
    # print(stores)
    desheve = min(stores, key= stores.get)
    desheva_cina = stores[desheve]
    # print(desheva_cina)

    doroge = max(stores, key= stores.get)
    doroga_cina = stores[doroge]

    medium_price = sum(stores.values()) / len(stores)

    print(f'min cina na {tovar} v {desheve} = {desheva_cina:.2f}')
    print(f'max cina na {tovar} = {doroga_cina:.2f}')
    print(f'medium cina na {tovar} = {medium_price:.2f}')
else:
    print('takoho tovaru nema')