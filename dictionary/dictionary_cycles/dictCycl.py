numbers = {
 1: "one",
 2: "two",
 3: "three"
}

for i in numbers.keys():
    print(i, end = ' ')

for i in numbers.values():
    print(i, end = ' ')

for i, j in numbers.items():
    print(f'key = {i}, value = {j}')

for i in numbers:
    numbers[i] = 5

print(numbers)


# Оголосити словник, що має наступну структуру «ключ» — номерний знак транспортного засобу (наприклад «АА2565ІН»), значення «власник авто» (наприклад, Іванов Іван)
# Додати в словник два нові авто
# Знайти власника за номером автомобіля
# Обійти словник і вивести прізвища людей, які мають більше одного авто

cars = {
    'ВЕ0988ВР': 'Ivan',
    '73811НІ': 'Mykhailo',
    'ВО1288ВН': 'Mykhailo',
}

cars['АА7777АА'] = 'Petro'
cars['ВК7412АО'] = 'Mykola'
cars['ВК74О'] = 'Mykola'

print(cars)

car = cars.get('7381НІ', 'NEma takih nomeriv')
print(car)

vlasniki = {}

for vlasnik in cars.values():
    if vlasnik in vlasniki:
        vlasniki[vlasnik] += 1
    else:
        vlasniki[vlasnik] = 1


for vl, count in vlasniki.items():
    if count > 1:
        print(f'{vl} mae {count} mashin')




# Створіть словник “stock”, який міститиме в собі (ключ — назва товару. Значення — кількість товару на складі). 
# Написати програму, яка запитує який товар та кількість, яку хоче купити користувач. 
# Вивести на екран True, якщо користувач може купити цей товар, якщо ні — False.

stock = {
    "apples": 50,
    "bananas": 20,
    "oranges": 30,
    "pears": 15
}

product = input('enter product ').lower()
kilkist = int(input('enter kilkist '))

if product in stock and stock[product] >= kilkist:
    print(True)


# Створіть словник, який містить дані про користувачів вашого веб-сайту. 
# Ключами в цьому словнику будуть імена користувачів, а значеннями — інформація про користувачів. 
# Попросіть користувача ввести імена користувачів, про яких хоче дізнатися інформацію, через пробіл. 
# Вивести інформацію про цих користувачів у форматі (Ім’я: вік, стать, електронна пошта).

users = {
    'lipa': {
        'age': 30,
        'gender': 'male',
        'email': 'abc@gmail.com',
    },
    'filipina': {
        'age': 10,
        'gender': 'female',
        'email': 'gggggg@gmail.com',
    },
    'john': {
        'age': 26,
        'gender': 'male',
        'email': '@gmail.com',
    }
}

username = input('Enter name or names(divided by space): ').split()

for usr in username:
    if usr in users:
          user_info = users[usr]
          print(f'{usr} - {user_info['age']} rokiv, {user_info['gender']}, {user_info['email']}')
    else:
     print('User or users not found')